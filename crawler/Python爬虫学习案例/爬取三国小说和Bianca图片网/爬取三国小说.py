import requests
from bs4 import BeautifulSoup
import os
import time
path='三国小说'#要存储的文件夹
main_url='https://www.shicimingju.com/book/sanguoyanyi.html'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
page_text=requests.get(url=main_url,headers=headers)
page_text.encoding='UTF-8'
page=page_text.text
#print(page)
#数据解析，章节标题，详情页url,章节内容
soup=BeautifulSoup(page,'lxml')
a_list=soup.select('.book-mulu>ul>li>a')
for i in a_list:
  title=i.string
  detail_url='http://www.shicimingju.com'+i['href']
  #print(title,detail_url)
#   #对详情页发起请求解析出章节内容
  page_detail=requests.get(url=detail_url,headers=headers)
  page_detail.encoding='UTF-8'
  page_detail=page_detail.text
  #print(page_detail)
  soup=BeautifulSoup(page_detail,'lxml')
  div_tag=soup.find('div',class_="chapter_content")
  content=div_tag.text
  # print(content)
  #数据持久化，存储小说
  if not  os.path.exists(path):
      os.mkdir(path)
  with open(path+'./%s'%title+'.txt','w',encoding='utf-8') as file:
        file.write(content+'\n')
        print("正在下载:"+title)
        time.sleep(2)
        file.close()