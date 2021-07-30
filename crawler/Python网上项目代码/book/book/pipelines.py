# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#coding: utf-8
import re
class BookPipeline:
    def process_item(self, item, spider):
    	# �����ݾ�ת�����ֵ�����
        item = dict(item)
        # �����ݽ�һ������ ʹ���ݸ�������
        if item['publish_date'] is not None:
            item['publish_date'] = re.sub(r'\xa0','',item['publish_date']).split(':')[-1]
        item['book_price'] = re.sub(r'��','',item['book_price'])
        print(item)
