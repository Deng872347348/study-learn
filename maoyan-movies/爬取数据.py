#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021年06月05日
# @File    : demo4.py

import requests
from fake_useragent import UserAgent
from lxml import etree
import time

# 随机请求头
ua = UserAgent()

# 构建请求 需要自己去网页上面换一下  请求不到了就 去网页刷新 把验证码弄了
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': '__mta=244176442.1622872454168.1622876903037.1622877097390.7; uuid_n_v=v1; uuid=6FFF6D30C5C211EB8D61CF53B1EFE83FE91D3C40EE5240DCBA0A422050B1E8C0; _csrf=bff9b813020b795594ff3b2ea3c1be6295b7453d19ecd72f8beb9700c679dfb4; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1622872443; _lxsdk_cuid=1770e9ed136c8-048c356e76a22b-7d677965-1fa400-1770e9ed136c8; _lxsdk=6FFF6D30C5C211EB8D61CF53B1EFE83FE91D3C40EE5240DCBA0A422050B1E8C0; ci=59; recentCis=59; __mta=51142166.1622872443578.1622872443578.1622876719906.2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1622877097; _lxsdk_s=179dafd56bf-06d-403-d81%7C%7C12',
    'User-Agent': str(ua.random)
}


def RequestsTools(url):
    '''
    爬虫请求工具函数
    :param url: 请求地址
    :return: HTML对象 用于xpath提取
    '''
    response = requests.get(url, headers=headers).content.decode('utf-8')
    html = etree.HTML(response)
    return html


def Index(page):
    '''
    首页函数
    :param page: 页数
    :return:
    '''
    url = 'https://maoyan.com/board/4?offset={}'.format(page)
    html = RequestsTools(url)
    # 详情页地址后缀
    urls_text = html.xpath('//a[@class="image-link"]/@href')
    # 评分
    pingfen1 = html.xpath('//i[@class="integer"]/text()')
    pingfen2 = html.xpath('//i[@class="fraction"]/text()')

    for i, p1, p2 in zip(urls_text, pingfen1, pingfen2):
        pingfen = p1 + p2
        urs = 'https://maoyan.com' + i
        # 反正请求太过于频繁
        time.sleep(2)
        Details(urs, pingfen)


def Details(url, pingfen):
    html = RequestsTools(url)
    dianyan = html.xpath('//h1[@class="name"]/text()') # 电影名称
    leixing = html.xpath('//li[@class="ellipsis"]/a/text()') # 类型
    diqu = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()') # 读取总和
    timedata = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()') # 时间
    for d, l, b, t in zip(dianyan, leixing, diqu, timedata):
        countyr = b.replace('\n', '').split('/')[0] # 地区
        shichang = b.replace('\n', '').split('/')[1] # 时长
        f = open('猫眼.csv', 'a')
        f.write('{}, {}, {}, {}, {}, {}, {}\n'.format(d, pingfen, url, l, countyr, shichang, t))
        print(d, pingfen, url, l, countyr, shichang, t )



if __name__ == '__main__':
    for page in range(0, 11):
        page *= 10
        Index(page)
