import scrapy
from lxml import etree
from ..items import HelloqiushiItem

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['qiushi.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    # def parse(self, response):
    #     #数据解析
    #     divs=response.xpath('//*[@id="qiushi_tag_124398008"]')
    #     for div in divs:
    #         author=div.xpath(".//div[1]/a[2]/h2/text()").get().strip()
    #         content=div.xpath(".//a[1]/div/span/text()").getall().strip()
    #         print(author)
    #         print(content)
    def parse(self, response):
        divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        items = []
        for div in divs:
            author = div.xpath("./div[1]/a[2]/h2/text()").extract_first()  # 当列表只有一个元素时,可以使用extract_first
            content = div.xpath("./a/div/span//text()").extract()
            content = "".join(content).strip("\n")
            # print(author, content)
            item = ScrapydemoItem()
            item['author'] = author
            item['content'] = content
            # items.append(item)
            yield item  # yield生成器,会把item发给pipeline
