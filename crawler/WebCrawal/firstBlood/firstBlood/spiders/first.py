from typing import List

import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件的名称：就是爬虫文件的一个唯一的标识
    name = 'first'
    #允许的域名
    #allowed_domains = ['www.baidu.com']
    #起始的url
    start_urls = ['https://www.baidu.com/','https://www.sogou.com']
    #用作于数据的解析：response参数是表示的就是请求成功后对应的响应对象
    def parse(self, response):
        #pass
        print(response)
