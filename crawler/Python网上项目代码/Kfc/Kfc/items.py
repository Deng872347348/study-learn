# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KfcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #门店编号，门店名称，所属城市，所属省份
    rownum=scrapy.Field()
    storeName=scrapy.Field()
    addressDetail=scrapy.Field()
    cityName=scrapy.Field()
    provinceName=scrapy.Field()

