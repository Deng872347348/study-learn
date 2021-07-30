import requests
import time
import json
# import os
import re
from lxml import etree
import time
urls = ['http://hwenhai-vpn01.eastasia.cloudapp.azure.com/#/?page={}'.format(i) for i in range(0,20)]
for url in urls:
    # path="美女写真集"
    headers = {
    'User - Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.212MobileSafari / 537.36',
    'Referer': 'http: // hwenhai - vpn01.eastasia.cloudapp.azure.com /',
    'X - Requested - With': 'XMLHttpRequest'
    }
    response = requests.get(url,headers=headers)
    response.encoding=response.apparent_encoding

    #解析网页的数据
    html=etree.HTML(response.text)

    #获取图片的名称
    picture_name=html.xpath("//article[@class='excerpt excerpt-c5']/div[@class='thumbnail']/h2/a/text()")
    # print(picture_name)
    #获取图片的链接:
    res = '<div class="imgbox" style="background-image:url(.*?)" '
    information = re.findall(res,response.text, re.S)
    # print(information)
    # 创建一个文件夹用来存储美女图片
    # if not os.path.exists(path):
    #     os.mkdir(path)
    for a,b in zip(information,picture_name):
        name=a.replace('(','').replace(')','')
        # print(name)
        #获取图片的链接
        href='http://hwenhai-vpn01.eastasia.cloudapp.azure.com'+name
        #再次发起请求，存储图片
        #休眠1秒
        time.sleep(1)
        picture_b=b+'.jpg'
        resp= requests.get(url=href, headers=headers)
        #对读取到的图片进行一个数据存储
        with open("美女写真集"+'./%s'%picture_b, 'wb') as f:
            f.write(resp.content)
            #打印提示信息，用来提示图片下载成功
            print(b+"下载成功")


