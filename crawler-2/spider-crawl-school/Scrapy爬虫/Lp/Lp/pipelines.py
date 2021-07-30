# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class LpPipeline(object):
    def __init__(self):
        self.file=open('liepin.json','w',encoding='utf-8')
        print("爬虫开始》》》》》》》》》》》》》")
    def process_item(self, item, spider):
        text=json.dumps(dict(item),ensure_ascii=False)
        self.file.write(text+'\n')
        print("QAQ------------>正在写入数据")
        return item
def close(self):
    print("爬虫结束了》》》》》》》》》》》》》》》")
    self.file.close()