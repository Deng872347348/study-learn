import requests
import re
import os
import urllib
dirName='ImgLibs'
if not os.path.exists(dirName):
  os.mkdir(dirName)
#捕获到当前首页的页面的源码数据
url='http://www.521609.com/qingchunmeinv/'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
page_text=requests.get(url=url,headers=headers).text
#从当前获取页面源码数据中解析出图片地址
ex='<li>.*?</img src="(.*?)" width=.*?</li>'
img_src_list=re.findall(ex,page_text,re.S)
#print(img_src_list)
for src in img_src_list:
   src='http://www.521609.com'+src
   imgPath=dirName+'/'+src.split('/')[-1]
   urllib.request.urlretrieve(src,)
   print(imgPath,"下载成功! ! !")