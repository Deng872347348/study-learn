# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说的名字
    name = scrapy.Field()
    #小说的作者
    author = scrapy.Field()
    # 小说的状态
    state = scrapy.Field()
    # 小说的简介
    description = scrapy.Field()
# 单独存放小说章节
class NovelItem2(scrapy.Item):
    tablename = scrapy.Field()
    title = scrapy.Field()
