import scrapy
import json
import re
from urllib.parse import urlencode
import scrapy
from ..items import ImagesItem
from  scrapy.http import Request
from fake_useragent import UserAgent
class A360Spider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['369.com']
    # start_urls = ['http://369.com/']
    headers = {'User-Agent': str(UserAgent().random)}
    def start_requests(self):
        base_url = 'https://image.so.com/j?'
        param = {}
        param['q'] = input("请输入关键词")
        param['sn'] = 130
        param['ps'] = 143
        url = base_url + urlencode(param)
        # yield关键字发请求
        yield Request(url=url, headers=self.headers, callback=self.parse)
    def parse(self, response):
            # 通过json库读取数据
            datas = json.loads(response.text)
            # 遍历数据
            for data in datas['list']:
                item = ImagesItem()
                item['id'] = data['id']  # 图片id
                item['title'] = data['title']
                item['url'] = data['img']  # 图片下载地址
                item['width'] = data['width']
                item['height']=data['height']
                print(item)
                # 发送item到管道文件
                yield item
