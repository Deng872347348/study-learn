import requests
from lxml import etree
from fake_useragent import UserAgent
import re
import redis
from hashlib import md5
import sys


class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36'
        }
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def get_html(self, url):
        """请求URL功能函数"""
        html = requests.get(url=url,
                            headers=self.headers).text

        return html

    def xpath_func(self, html, xpath_bds):
        """xpath提取功能函数"""
        eobj = etree.HTML(html)
        r_list = eobj.xpath(xpath_bds)

        return r_list

    def md5_url(self, url):
        """md5加密功能函数"""
        s = md5()
        s.update(url.encode())

        return s.hexdigest()

    def parse_html(self):
        html = self.get_html(url=self.url)
        # 提取最新月份的href
        xpath_bds = '//table/tr[1]/td[@class="arlisttd"]/a/@href'
        href_list = self.xpath_func(html, xpath_bds)
        if href_list:
            two_url = 'http://www.mca.gov.cn' + href_list[0]
            finger = self.md5_url(two_url)
            if self.r.sadd('mzb:spiders', finger) == 1:
                # 提取详情页的具体数据
                self.get_data(two_url)
            else:
                sys.exit('网站未更新')
        else:
            print('提取最新链接失败')

    def get_data(self, two_url):
        """提取具体数据"""
        # 1.在two_html中提取跳转之后的真实链接
        false_html = self.get_html(url=two_url)
        regex = 'window.location.href="(.*?)"'
        pattern = re.compile(regex, re.S)
        true_url_list = pattern.findall(false_html)
        if true_url_list:
            true_url = true_url_list[0]
            true_html = self.get_html(url=true_url)
            # 2.向真实链接发请求,拿到响应内容
            two_xpath = '//tr[@height="19"]'
            tr_list = self.xpath_func(true_html, two_xpath)
            for tr in tr_list:
                item = {}
                item['name'] = tr.xpath('./td[3]/text()')[0]
                item['code'] = tr.xpath('./td[2]/text() | ./td[2]/span/text()')[0]
                print(item)
        else:
            print('真实链接提取失败')

    def run(self):
        self.parse_html()


if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()

