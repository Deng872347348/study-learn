import requests
from lxml import etree
from pymongo import MongoClient
base_url="https://mongoing.com/page/"
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
end_page=input("请输入加载的页数")
content=[]
for page in range(1,int(end_page)+1):

    url=base_url+str(page)
    response=requests.get(url,headers=headers)
    html=response.text
    tree=etree.HTML(html)
    titles=tree.xpath("//div[@class='content']/article/header/h2/a/text()")
    print(titles)
    times=tree.xpath("//p[@class='meta']/time/text()")
    print(times)
    authors=tree.xpath("//p[@class='meta']/span[@class='author']/text()")
    print(authors)
    comments=tree.xpath("//p[@class='meta']/a[@class='pc']/text()")
    print(comments)
    notes=tree.xpath("//p[@class='note']/text()")
    url_data={
        'url':url,
        'page':page
    }
    content.append(url_data)
for i in range(0,len(titles)):
         title=titles[i]
         time=times[i]
         author=authors[i]
         comment=comments[i]
         note=notes[i]
         data={
             'id':i+1,
             'title':title,
             'time':time,
             'author':author,
             'comment':comment,
             'note':note
         }
         content.append(data)
print(content)

#连接mongodb数据库
client=MongoClient('localhost',27017)

#创建数据库
db=client.mongodb_database

#创建集合
columns=db.infos
#存储数据到数据库中
#插入数据
columns.insert_many(content)

#查询一条数据
find_one=columns.find_one({'page':1})

#查询所有数据
# find_all=columns.find

#查询带条件的所有数据
# find_all=columns.find({'id':1})
#查询id>7  $lt


