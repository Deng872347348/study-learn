# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ImagesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()           #设置图片id
    title = scrapy.Field()  # 设置图片标题
    url=scrapy.Field()     #设置图片url
    width =scrapy.Field()
    height=scrapy.Field()


