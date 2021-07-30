import scrapy
import json
from ..items import SoItem
class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url='https://image.baidu.com/user/logininfo?src=pc&page=searchresult&time=1616321646504'
    def start_requests(self):
        #生成所有要抓取的URL地址
        for sn in range(30,151,30):
            page_url=self.url.format(sn)
            yield  scrapy.Request(url=page_url,callback=self.parse)

    def parse(self, response):
        #提取图片链接s
        html=json.loads(response.text)
        for one_image_dict in html['adType']:
            item=SoItem()
            item['image_url']=one_image_dict['hoverURL']
            item['image_title']=one_image_dict['fromPageTitleEnc']
            #图片链接提取完成，直接交给管道文件就行
            yield item