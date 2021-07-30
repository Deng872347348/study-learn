# 导入数据架包
import os
import re

import requests

if __name__:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    # 创建一个文件夹，将图片存在里面
    if not os.path.exists('./Dengbo'):
        os.mkdir('./DengLibs')
        url = "https://www.bilibili.com/"
        #设置一个通用的url的模板
        pageNum=2
        for pageNum in range(1,36):
            #对应页码的url
            new_url=format(url%pageNum)
        page_text = requests.get(url=new_url, headers=headers).text
#数据的一个解析过程
#<div class="zhuanji-inner-box zhuanji-img" style="background:url(.*?);"><\/div>
ex = '<div class="zhuanji-inner-box zhuanji-img" style="background:url(.*?);"><\/div>'
img_src_lisy = re.findall(ex, page_text, re.S)
# 拼接图片的地址
for src in img_src_lisy:
    src = 'http:' + src
    # 请求图片的二进制的数据
    img_data = requests.get(url=url, headers=headers).content
    # 生成图片的名称
    img_name = src.split('/')[-1]
    # 生成图片的一个路径
    imgPath = './DengLibs' + img_name
    # 数据的持久化
    with open(imgPath, 'wb') as fp:
        fp.write(img_data)
        print(img_name, '下载成功!!!')
#bas4

#实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
#通过调用BeautifulSoup对象属性或者方法进行标签的定位和数据提取

# 环境的按照
# pip install bs4
# pip install lxml
# 如何实例化BeautifulSoup对象：
# from bs4 import  BeautifulSoup
# 对象的实例化：
# 1.将本地的html文档中的数据加载到该对象中
#  fp=open('./test.html','r',encoding='utf-8)
#          soup=BeautifulSoup(fp,'lxml')
# 2.将互联网上获取的页码源码加载到该对象中
#    page_text=response.text
#    soup=BeautifulSoup(page_text,'lxml')
#    提供的用于数据解析的方法和属性
#    soup.tagName:返回的是文档中第一次出现的tagName对应的标签、
# soup.find():
# find('tagName'):等同于soup.div
# 属性定位：
# soup.find('div',class_id/attr='song')
# soup.find_all('tagName'):返回符合要求的所有标签(列表)
# select:
# select('id','class'标签....选择器)返回的是一个列表
# 星级选择器：
# soup.select('div>ul>a>')表示一个层级
# soup.select('.tang>ul  a')空格表示多个层级
# 获取标签的文本数据
# soup.a.text/string/get_text()
# text/get_text可以获取一个标签所有的文本的内容
# string只可以获取该标签直系下的文本内容
# 获取该标签中属性值:
# 获取标签属性值
# soup.a['href']


