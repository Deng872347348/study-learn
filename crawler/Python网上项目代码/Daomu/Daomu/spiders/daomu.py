import scrapy
from ..items import DaomuItem
import os
class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    # start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
       # 一级页面解析函数，提取数据
       a_list=response.xpath('//li[contains(id,"menu-item-")]/a')
       for a in a_list:
           item=DaomuItem()
           item['parent_title']=a.xpath('./text()').get()
           parent_href=a.xpath('./@href').get()
            #创建对应的目录结构
           directory='./novel/{}/'.format(item['parent_title'])
           if not os.path.exists(directory):
               os.mkdir(directory)
           #将parent_href继续交给调度器入队列
           yield scrapy.Request(url=parent_href,meta={'item':item},callback=self.parse_second_page)
    def parse_second_page(self,response):
        # 二级页面解析函数
        meta1= response.meta['item']
        a_list=response.xpath('//article/a')
        for a in a_list:
            #创建全新的item对象，避免在给对象赋值时一直被覆盖
            item=DaomuItem()
            item['son_title']=a.xpath('./text()').get()
            item['parent_title']=meta1['parent_title']
            son_href=a.xpath('./@href').get()
            yield scrapy.Request(url=son_href,meta={"item":item},callback=self.parse_third_page)
    def parse_third_page(self,response):
        # 三级页面解析函数
        item=response.meta['item']
        p_list=response.xpath('//article/p/text()').extract()
        item['novel_content']='\n'.join(p_list)

        yield item
        #至此，一本完整的小说数据提取就完成
