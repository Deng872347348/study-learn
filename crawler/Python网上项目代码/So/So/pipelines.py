# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class SoPipeline(ImagesPipeline):
    #重写get_media_requests()方法，将图片链接交给调度器入队列就可以
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['image_url'],meta={'title':item['image_title']})
    #重写file_path(self,requests,response=None,info=None):
    def file_path(self, request, response=None, info=None):
        image_title=request.meta['title']
        filename=image_title+'.jpg'

        return filename