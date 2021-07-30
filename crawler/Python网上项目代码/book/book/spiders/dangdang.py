
#coding: utf-8
import urllib.parse
from copy import deepcopy

import scrapy


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/']

    def start_requests(self):
    # 设置响应头 博主测试过没有配置Referer请求会被拦截
        headers = {
            "Referer":"http://book.dangdang.com/",
        }
        yield scrapy.Request(self.start_urls[0], headers=headers, callback=self.parse)

    def parse(self, response):
  		# 根据图书大分类进行分组 如图李1所示
        div_list = response.xpath('//div[@id="floor_1"]/div[@class="classify_kind"]')
        for div in div_list:
            item = {}
            item['b_cate'] = div.xpath('./div/a/text()').get()
            ul_list = div.xpath('./ul/li')
            # 根据图书小分类进行分组 如图例2所示
            for li in ul_list:
                item['s_cate'] = li.xpath('./a/text()').get()
                item['s_href'] = li.xpath('./a/@href').get()
                #deepcopy对数据进行深拷贝  由于scrapy是异步请求模式 使用深拷贝可以防止数据备覆盖
                yield scrapy.Request(item['s_href'], self.parse_book_list, meta={'item': deepcopy(item)})
	# 对图书列表页进行解析
    def parse_book_list(self, response):
        item = response.meta['item']
        book_list = response.xpath('//ul[@class="bigimg"]/li')
        # 对每一本图书进行分组 如图例三所示
        for li in book_list:
            item['book_name'] = li.xpath('./a/@title').get()
            item['book_img'] = li.xpath('./a/img/@src').get()
            if item['book_img'] is not None:
                item['book_img'] = urllib.parse.urljoin(response.url,item['book_img'])
            item['book_url'] = li.xpath('./a/@href').get()
            item['book_price'] = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()').get()
            yield scrapy.Request(item['book_url'], self.parse_book_detail, meta={'item': deepcopy(item)})
        # 进行翻页操作
        next_url = response.xpath('//a[text()="下一页"]/@href').get()
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url,next_url)
            yield scrapy.Request(next_url,self.parse_book_list,meta={'item':item})
	# 对图书详情页进行解析
    def parse_book_detail(self, response):
        item = response.meta['item']
        item['author'] = response.xpath('//div[@class="messbox_info"]/span[1]/a/text()').get()
        item['book_press'] = response.xpath('//div[@class="messbox_info"]/span[2]/a/text()').get()
        item['publish_date'] = response.xpath('//div[@class="messbox_info"]/span[3]/text()').get()
        yield item
