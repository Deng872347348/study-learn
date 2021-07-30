# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from .pipelines import ScrapydemoPipeline
class HelloqiushiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #爬取的字段
    author=scrapy.Field()
    content=scrapy.Field()
