# import urllib.request
# #1.确定爬取得网址
# import urllib
# url="https://ys.mihoyo.com/?utm_source=adlenovo&from_channel=adlenovo#/"
# #请求https://ys.mihoyo.com/?utm_source=adlenovo&from_channel=adlenovo#/
# response=urllib.request.urlopen(url)
# print(response)
# #3网络相应http://www.baidu.com/
# html=response.read().decode()#解码 bytes转成str
# print(html)
# #数据存储
# with open("baidu.html",'w',encoding='utf-8')as f:
#     f.write(html)

#
# import requests
#
# url='https://pic.netbian.com/4kdongman/'
# html=requests.get(url)
#
# html=html.content.decode('UTF-8')
# print(html)
#
# with open("biantp.html",'w',encoding='utf-8')as f:
#      f.write(html)


import requests
url = 'https://www.sogou.com/web'
headers = {
'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.182Safari / 537.36Edg / 88.0.705.81'
}
wd=input('请输入搜索关键字')
param={
  'query':wd
}
response = requests.get(url=url, headers=headers, params=param).text
with open('sougouSearch.html','w',encoding='utf-8') as fp:
   fp.write(response)
print('写入完成')

