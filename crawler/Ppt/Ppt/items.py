# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PptItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #定义什么？？管道文件需要什么？
    class_name=scrapy.Field()
    ppt_name=scrapy.Field()
    ppt_download_url=scrapy.Field()
