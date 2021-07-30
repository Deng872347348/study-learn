import requests
import re
import time
import random
from fake_useragent import UserAgent
import pymongo
import redis
from hashlib import md5
import sys

class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'
        # mongodb的3个对象
        # 连接到mongodb
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['cardb']
        self.myset = self.db['carset']
        # 连接到redis
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        # ignore参数: 解码时遇到不识别的字符直接忽略掉
        html = requests.get(url=url, headers=headers).content.decode('gb2312', 'ignore')

        return html
    def re_func(self, regex, html):
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)

        return r_list

    def md5_url(self, url):
        s = md5()
        s.update(url.encode())

        return s.hexdigest()

    def parse_html(self, one_url):
        one_html = self.get_html(url=one_url)
        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        # href_list: ['/declear/xxx.html', '', '', '', ...]
        href_list = self.re_func(one_regex, one_html)
        for href in href_list:
            finger = self.md5_url(href)
            # 返回值1:之前没抓过
            if self.r.sadd('car:spiders', finger) == 1:
                # 拼接完整URL地址,发请求提取具体汽车信息
                self.get_one_car_info(href)
                time.sleep(random.randint(1, 2))
            else:
                # 一旦发现之前抓过的,则彻底终止程序
                sys.exit('更新完成')

    def get_one_car_info(self, href):
        two_url = 'https://www.che168.com' + href
        two_html = self.get_html(url=two_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span.*?(?:"overlayPrice">|"price">)(.*?)(?:<b>|</span>)'
        # car_info_list:
        # [('宝马','12万公里','2004年','自动/2.5L','北京','4.20')]
        car_info_list = self.re_func(two_regex, two_html)
        item = {}
        item['name'] = car_info_list[0][0].strip()
        item['km'] = car_info_list[0][1].strip()
        item['time'] = car_info_list[0][2].strip()
        item['type'] = car_info_list[0][3].split('/')[0].strip()
        item['displace'] = car_info_list[0][3].split('/')[1].strip()
        item['address'] = car_info_list[0][4].strip()
        item['price'] = car_info_list[0][5].strip()

        print(item)
        # 数据存入到MongoDB数据库
        self.myset.insert_one(item)

    def run(self):
        for page in range(1, 5):
            page_url = self.url.format(page)
            self.parse_html(page_url)

if __name__ == '__main__':
    spider = CarSpider()
    spider.run()
