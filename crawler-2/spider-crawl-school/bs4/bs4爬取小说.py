import requests
from bs4 import BeautifulSoup
import  re
import os
import  time
# def yuanzun(url):

url='http://book.zongheng.com/showchapter/685640.html'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'
        }
response = requests.get(url=url,headers = headers)
soup = BeautifulSoup(response.text,'html.parser')
novel_title=soup.select('div.volume-list > div:nth-child(2) > ul > li> a')
# print(novel_title)
item=[]
path='元尊'
if not os.path.exists(path):
    os.mkdir(path)
for i in range(len(novel_title)):
    novel_href=novel_title[i].attrs['href']
    # print(novel_href)
    # item.append(novel_href)
    time.sleep(3)
    resp=requests.get(url=novel_href,headers=headers).text

    soup = BeautifulSoup(resp, 'html.parser')
    div = soup.select("#readerFt > div > div.content")
    title = soup.select("#readerFt > div > div.title > div.title_txtbox")
    souptitle = BeautifulSoup(str(title),'html.parser').text.strip("[]")
    souptext = BeautifulSoup(str(div),'html.parser').text.strip("[]").replace("。","。\n")
    with open(path+'/%s'%(souptitle),'a',encoding='utf-8') as f:
                f.write(str(souptitle)+'\r')
                f.write(str(souptext)+'\r')
                print(souptext+"爬取成功")
                f.close()

