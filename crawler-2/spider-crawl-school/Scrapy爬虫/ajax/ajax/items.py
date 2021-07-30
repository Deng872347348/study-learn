# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AjaxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    jobMoney = scrapy.Field()
    jobNeed = scrapy.Field()
    jobCompany = scrapy.Field()
    jobType = scrapy.Field()
    jobSpesk = scrapy.Field()
