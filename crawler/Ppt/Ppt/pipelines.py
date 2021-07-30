# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
import os
from scrapy.pipelines.files import FilesPipeline
class PptPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        # 将文件下载链接交给调度器入队列
        yield  scrapy.Request(url=item['ppt_download_url'],meta={'item':item})
    def file_path(self, request, response=None, info=None):
        item=response.meta['item']
            #filename:工作总结PPT/绿色小清新工作总结ppt.zip
        filename='{}/{}'.format(
            item['class_name'],
            item['ppt_name'],
            os.path.splitext(item['ppt_download_url'])[1]

        )
        return filename
        # def process_item(self, item, spider):
    #     return item
