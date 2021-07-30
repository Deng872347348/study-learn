import  requests
from  lxml import etree
url='https://music.163.com/#/discover/toplist?id=19723756'

headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
response=requests=requests.get(url,headers=headers)
html=response.text
print(html)
#3.删选数据,音乐文件
list=html.xpath('//a[contains(@href, "song?")]')

#提取a标签的蓝色部分
# for data in list:
#     href=data.xpath('./@href')[0]
#     print(href)
#     id=href.split("#")[1]
#     #获取音乐的名字
#     data.xpath('./text()')[0]
#     url_base='http://music.163.com/song/media/outer/url?id='
#
#     #获取音乐数据
#     music=requests.get(url_base+id,headers=headers)
#
#     with open('music/'+music+".mp3",'wb') as f:
#         f.write(music.content)
