import scrapy
from scrapydemo.items import ScrapydemoItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'  #爬虫的唯一标识
    allowed_domains = ['www.qiushibaike.com']
    #爬虫开始的入口url
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        #数据解析
        divs=response.xpath('//div[@class="col1 old-style-col1"]/div')
        #items=[]
        for div in divs:
             author=div.xpath("./div[1]/a[2]/h2/text()")[0].extract()
             #当列表只有一个selector元素时，可以extract_first()
             #author=div.xpath("./div[1]/a[2]/h2/text()").extract_first()
             content=div.xpath("./a/div/span//text()").extract() #返回的列表
             content="".join(content).strip("\n")
             #print(author,content)
             item=ScrapydemoItem()
             item['author']=author
             item['content']=content
            # items.append(item)
             yield item   #yield生成器，会把item发送给管道文件pipline