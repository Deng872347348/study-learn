# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
class DaomuPipeline(object):
    def process_item(self, item, spider):
        #路径:./novel/parent_title
        filename='./novel/{}/{}.txt'.format(
            item['parent_title'].replace(':','_'),
            item['son_title'].replace(' ','_')
        )
        with open(filename,'w') as f:
            f.write(item['novel_content'])
        return item
