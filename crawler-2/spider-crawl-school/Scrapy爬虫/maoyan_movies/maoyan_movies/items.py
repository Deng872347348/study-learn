# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class MaoyanMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #编写要存储的字段
    #电影名字
    name = scrapy.Field()
    #主演明星
    starts = scrapy.Field()
    #上映时间
    releasetime = scrapy.Field()
    #评分
    score = scrapy.Field()
