import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MaoyanItem

class MyspiderSpider(CrawlSpider):
    name = 'myspider'
    # allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=0']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MaoyanItem()
        # 影片名字
        item['name'] = response.xpath("//p[@class='name']/a/text()").extract()[0]
        #主演
        actor = response.xpath("//div[@class='movie-item-info']/p[@class='star']/text()").extract()[0].strip()
        # 上映时间
        item['releasetime'] = response.xpath("//div[@class='movie-item-info']/p[@class='releasetime']/text()").extract()[0]
        # # 影片时间
        # item['time'] = response.xpath('//li[@class="ellipsis"][2]/text()').extract()[0].strip()[-5:]
        # 评分
        item['score'] = response.xpath("//dl/dd/div/div/div[2]/p/i").extract()[0]
        # 图片链接
        item['image'] = response.xpath("//img[@class='board-img']/@src").extract()[0]
        print(item['name'])
        print(item['actor'])
        print(item['score'])
        print(item['image'])
        yield item
