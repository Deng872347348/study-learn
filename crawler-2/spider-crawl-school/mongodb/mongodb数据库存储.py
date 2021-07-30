import requests
import sys
import re  #用于正则化操作
from lxml import etree
from fake_useragent import UserAgent
#上述用于爬虫
import pymongo as pm    #链接mongoDB

client = pm.MongoClient()
db = client['face']   #访问数据库
collection = db['my_face']  #访问表

headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
          }

#遍历页面，对详情页面的一个数据的提取
for j in range(1, 5000):
    content1 = requests.get('http://star.ifensi.com/s{}/'.format(j), headers=headers).text
    # print(content1)
    root1 = etree.HTML(content1)
    # print(root1)
    href1 = root1.xpath('//div[@class="hbox clearfix"]/div[@class="hd_1"]/img')  # 定位到img标签

    name = root1.xpath("//h1[@class='t1']/text()")  # 获得明星的名字
    birth = root1.xpath("//p[@class='t2'][1]//text()")  # 获得明星的身高和生日
    data = {}
    try:
        data["name"] = name[0]  # 这一步是为了排除无法访问的网站，如果网站无法访问直接进入下一循环
    except:
        continue
    data["id"] = j
    for i in range(len(birth)):
        birth[i] = birth[i].replace("\xa0", "")  # 去空格
        hanzi, number = re.findall('(.*)：(.*)', birth[i])[0]  # 分别提取出key和value
        data[hanzi] = number  # 在字典中创建键值对

    img_url = href1[0].attrib["src"]  # 获取图片的url

    response = requests.get(img_url, headers=headers)

    img = response.content
    with open('faces/{}.jpg'.format(j), 'wb') as f:
        f.write(img)  # 将图片保存到faces文件夹
    data["path"] = 'faces/{}.jpg'.format(j)  # 保存相对路劲

    collection.insert_one(data)  # 将字典插入到表中




