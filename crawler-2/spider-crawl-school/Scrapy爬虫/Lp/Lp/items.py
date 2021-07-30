# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #岗位名称
    name=scrapy.Field()
    #公司
    company=scrapy.Field()
    #职位信息
    info=scrapy.Field()
    #投递时间1反馈
    time=scrapy.Field()
