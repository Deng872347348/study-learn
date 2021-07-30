import scrapy


class SpidernameSpider(scrapy.Spider):
    name = 'spiderName'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
