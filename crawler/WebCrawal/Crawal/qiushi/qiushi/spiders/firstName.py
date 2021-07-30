import scrapy


class FirstnameSpider(scrapy.Spider):
    name = 'firstName'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
