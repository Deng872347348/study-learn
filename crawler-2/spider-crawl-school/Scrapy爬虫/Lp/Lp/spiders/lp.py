import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from bs4 import BeautifulSoup
from ..items import LpItem
class LpSpider(CrawlSpider):
    name = 'lp'
    # allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?init=-1&headckid=557b501fed09896f&fromSearchBtn = 2 & sfrom = click - pc_homepage - centre_searchbox - search_new & ckid = 557b501fed09896f& degradeFlag = 0 & key = python & siTag = I - 7rQ0e90mv8a37po7dV3Q % 7EfA9rXquZc5IkJpXC - Ycixw & d_sfrom = search_fp & d_ckId = 3d61d864d3db13448f1adb929ce4f2c3 & d_curPage = 0 & d_pageSize = 40 & d_headId = 3d61d864d3db13448f1adb929ce4f2c3 & curPage = 0']
    #定义提取超链接的提取规则
    page_link=LinkExtractor(allow=("&curPage=\d+"))
    #定义爬取数据的规则
    rules=(
        Rule(page_link,callback='parse_item',follow=True),
    )
    def parse_item(self, response):
        item=LpItem()
        #获取招聘信息列表
        soup=BeautifulSoup(response.text,'lxml')
        job_list=soup.select('ul.sojob-list li')
        for job in job_list:
            item['name']=job.find('div',class_='job-info').h3.attrs['title']
            item['company']=job.find('p',class_='company-name').a.text
            item['info']=job.find('p',class_='condition clearfix').attrs['title']
            item['time']=job.find('p',class_="time-info clearfix").span.text
            # print(item)
            yield item

