import requests
from lxml import etree
from IPPool import Pool
import random
from  fake_useragent import  UserAgent
headers = {
    'User-Agent':UserAgent().random}
for i in range(10):
    pool = random.choice(Pool())  # 获取IPPool中的数据
    proxyHost = pool['ip']  # 获取IP
    proxyPort = pool['port']  # 获取端口号

    targetUrl = 'https://ip.tool.chinaz.com/'

    proxyMeta = "http://%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
    }
    print(proxyMeta)

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    # print(proxies)/
    try:
        resp = requests.get(targetUrl, headers=headers, proxies=proxies, timeout=5)
        resp.encoding = resp.apparent_encoding
        sel = etree.HTML(resp.text)
        # print(resp.text)
        ip = sel.xpath('//*[@id="rightinfo"]/div[1]/dl/dd[1]/text()')[0]  # IP地址
        addr = sel.xpath('//*[@id="rightinfo"]/div[1]/dl/dd[2]/text()')[0]  # 来自
        print(ip + '\t' + addr)
        print('*'*30)
    except Exception as e:
        print(e)
