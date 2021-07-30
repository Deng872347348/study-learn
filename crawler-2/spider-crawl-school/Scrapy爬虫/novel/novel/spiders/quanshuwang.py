import scrapy
import re
from scrapy.http import Request
from ..items  import NovelItem
from ..items import NovelItem2
class QuanshuwangSpider(scrapy.Spider):
    name = 'quanshuwang'
    # allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/list/1_1.html']
    # start_urls = ['http://127.0.0.1:8000/list/1_1.html']  # 全书网玄幻魔法类第一页
    # 1.定义函数，通过'马上阅读'获取每一本书的 URL
    def parse(self, response):
        book_urls = response.xpath('//li/a[@class="l mr10"]/@href').extract()
        three_book_urls = book_urls[0:3]  # 只取3本
        for book_url in three_book_urls:
            yield Request(book_url, callback=self.parse_read)

    # 2.定义函数，进入小说简介页面，获取信息，得到后yield返回给pipelines处理，并获取'开始阅读'的url，进入章节目录
    def parse_read(self, response):
        item = NovelItem()
        # 小说名字
        name = response.xpath('//div[@class="b-info"]/h1/text()').extract_first()
        # 小说简介
        description = response.xpath('//div[@class="infoDetail"]/div/text()').extract_first()
        # 小说连载状态
        state = response.xpath('//div[@class="bookDetail"]/dl[1]/dd/text()').extract_first()
        # 作者名字
        author = response.xpath('//div[@class="bookDetail"]/dl[2]/dd/text()').extract_first()
        item['name'] = name
        item['description'] = description
        item['state'] = state
        item['author'] = author
        yield item
        # 获取开始阅读按钮的URL，进入章节目录
        read_url = response.xpath('//a[@class="reader"]/@href').extract()[0]
        yield Request(read_url, callback=self.parse_info)
    # 3.定义函数，进入章节目录，获取小说章节名并yield返回
    def parse_info(self, response):
        item = NovelItem2()
        tablename = response.xpath('//div[@class="main-index"]/a[3]/text()').extract_first()
        titles = response.xpath('//div[@class="clearfix dirconone"]/li')
        for each in titles:
            title = each.xpath('.//a/text()').extract_first()
            item['tablename'] = tablename
            item['title'] = title
            yield item

