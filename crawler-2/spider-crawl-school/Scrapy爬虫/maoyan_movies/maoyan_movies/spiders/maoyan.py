import scrapy
from ..items  import MaoyanMoviesItem
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    offset = 0
    url = "https://maoyan.com/board/4?offset="
    # 1.对url进行定制，为翻页做准备
    start_urls = [url + str(offset)]
    # 2.定义爬虫函数parse()
    def parse(self, response):
        item =MaoyanMoviesItem()
        movies = response.xpath("//div[ @class ='board-item-content']")
        for each in movies:
            # 电影名
            name = each.xpath(".//div/p/a/text()").extract()[0]
            # 主演明星
            starts = each.xpath(".//div[1]/p/text()").extract()[0]
            # 上映时间
            releasetime = each.xpath(".//div[1]/p[3]/text()").extract()[0]
            score1 = each.xpath(".//div[2]/p/i[1]/text()").extract()[0]
            score2 = each.xpath(".//div[2]/p/i[2]/text()").extract()[0]
            # 评分
            score = score1 + score2
            item['name'] = name
            item['starts'] = starts
            item['releasetime'] = releasetime
            item['score'] = score
            yield item
        # 3.在函数的最后offset自加10，然后重新发出请求实现翻页功能
        if self.offset < 90:
            self.offset += 10
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
