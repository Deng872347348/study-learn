# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapydemoPipeline:
    fp = None
    def open_spider(self, spider):
        self.fp = open('qiubai.txt','w',encoding='utf-8')
        print("爬虫开始爬取了")

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        data = author+":"+content+"\n"
        self.fp.write(data)
        return item
    def close_spider(self,spider):
        print("爬虫完成了")
        self.fp.close()
