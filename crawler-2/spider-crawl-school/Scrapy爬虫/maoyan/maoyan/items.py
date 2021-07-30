# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 影片中文名称/英文名称
    ztitle = scrapy.Field()
    etitle = scrapy.Field()
    # 影片类型
    type = scrapy.Field()
    # 导演
    dname = scrapy.Field()
    # 主演
    star = scrapy.Field()
    # 上映时间
    releasetime = scrapy.Field()
    # 影片时间
    time = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 图片链接
    image = scrapy.Field()
    # 详情信息
    info = scrapy.Field()
