import requests
from lxml import etree
from  bs4 import  BeautifulSoup
from pymongo import MongoClient
#确定爬取的网址
url="http://finance.people.com.cn/n1/2020/0316/c1004-31632742.html"
#构建消息头
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
#发送
response=requests.get(url,headers=headers)
html=response.content.decode("GBK")

#利用beautifulsoup对页面进行解析
soup=BeautifulSoup(html,'lxml')
#标题
title=soup.h1.text
# print(title)
#副标题
sub=soup.find('h4',class_='sub').text
# print(sub)
#时间
time=soup.select('div.channel.cf > div.col-1-1.fl')[0].text
# print(time)
#作者
author=soup.select('div.col.col-1.fl > div.author.cf')[0].text
# print(author)
#文章内容
article=soup.select('div.rm_txt_con.cf > p')
content=""

for value in article:
    content+=value.text.strip()
# print(content)
#组合数据
data={
    'title':title,
    'sub':sub,
    'author':author,
    'content':content
}
print(data)
#连接mongodb数据库进行存储

client=MongoClient('mongodb://localhost:27017/')

#以数据字典的形式
db=client['test_database']
#以数据字典
column=db['article']
#插入数据
result=column.insert_one(data)
print(result)


