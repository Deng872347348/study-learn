import scrapy
from HelloCSDN.items import HellocsdnItem
from  ..items import HellocsdnItem
class CsdnSpider(scrapy.Spider):
    name = 'CSDN'
    allowed_domains = ['www.csdn.net']
    start_urls = ['https://blog.csdn.net/qq_17623363/article/details/108775998']
    #数据解析
    def parse(self, response):
        #数据解析
        divs=response.xpath('//*[@id="content_views"]')
        #items=[]
        for div in divs:
             name=div.xpath('./h1/text()').extract()
             #当列表只有一个selector元素时，可以extract_first()
             #author=div.xpath("./div[1]/a[2]/h2/text()").extract_first()
             content=div.xpath("./p/text()").extract() #返回的列表
             content="".join(content).strip("\n")
             item =HellocsdnItem()
             item['name'] = name
             item['content'] = content
             # items.append(item)
             yield item  # yield生成器，会把item发送给管道文件pipline
