import scrapy
from scrapy.http import Request
import requests
from ..items import AjaxItem
class AjaxSpider(scrapy.Spider):
    name = 'Ajax'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/%d/' % n for n in range(1, 6)]
    #定义爬虫处理函数parse()
    def parse(self, response):
        Jobs = response.xpath('//ul[@class="item_con_list"]/li')
        for Job in Jobs:
            jobName = Job.xpath('div/div/div/a/h3/text()').extract_first()
            jobMoney = Job.xpath('div/div/div/div/span/text()').extract_first()
            jobNeed = Job.xpath('div/div/div/div/text()').extract()
            jobNeed = jobNeed[2].strip()
            jobCompany = Job.xpath('div/div/div/a/text()').extract()
            jobCompany = jobCompany[3].strip()
            jobType = Job.xpath('div/div/div/text()').extract()
            jobType = jobType[7].strip()
            jobSpesk = Job.xpath('div[@class="list_item_bot"]/div/text()').extract()
            jobSpesk = jobSpesk[-1].strip()
            item = AjaxItem()
            item['jobName'] = jobName
            item['jobMoney'] = jobMoney
            item['jobNeed'] = jobNeed
            item['jobCompany'] = jobCompany
            item['jobType'] = jobType
            item['jobSpesk'] = jobSpesk
            yield item