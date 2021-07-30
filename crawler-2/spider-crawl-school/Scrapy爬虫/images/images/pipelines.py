# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import pymongo
from  scrapy.http import Request
class ImagesPipeline(ImagesPipeline):
    #获取图片的路径
    def file_path(self, request, response=None, info=None, *, item=None):
         url=request.url
         file_path=url.split("/")[-1]
         return file_path
    #发起请求，获取图片
    def get_media_requests(self, item, info):
        yield Request(url=item['url'])
    def item_completed(self, results, item, info):
        image_paths=[x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('下载失败')
        return item
class ImagesPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url=mongo_url
        self.mongo_db=mongo_db
    #如何从配置文件setting读取数据库的配置赋值给实例对象
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url=crawler.settings.get("MONGO_URL"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_url)
        self.db=self.client[self.mongo_db]
    def process_item(self,item,spider):
        self.db[spider.name].insert(dict(item))
        print("数据库中集合的名字:"+spider.name)
        return item
    def close_spider(self,spider):
        self.client.close()
