import scrapy
from bs4 import BeautifulSoup
from ..items import HelloweeklyItem

class QiwuSpider(scrapy.Spider):
    name = 'qiwu'
    allowed_domains = ['qiwu.cn']
    start_urls = ['https://weekly.75.team/']

    def parse(self, response):
        # 持久化
        with open('weekly.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
            # 数据解析
            soup = BeautifulSoup(response.text, 'lxml')
            # 目标元素
            li_list = soup.select('ol.issue-list li')
            items = []
            # 循环获取行元素
            for li in li_list:
                # 将获取的对象封装到Helloweekly
                item = HelloweeklyItem()
                name = li.a.text
                time = li.find('time', class_='date').text
                # 构造数据
                item['name'] = name
                item['time'] = time
                items.append(item)
            return items
