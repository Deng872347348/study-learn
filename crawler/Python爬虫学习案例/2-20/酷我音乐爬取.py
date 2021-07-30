import requests
import time
url='http://www.kuwo.cn/api/www/search/searchKey?key=&httpsStatus=1'
#请求头
headers={
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
   'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1611144741; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1611144741; _ga=GA1.2.218053802.1611144741; _gid=GA1.2.989913331.1611144741; _gat=1; kw_token=B3R2OY03HG8''csrf': 'B3R2OY03HG8'
}
repsonse=requests.get(url,headers=headers,timeout=3).json()
print(repsonse)
data=repsonse['data']['musiclist']
for i in data:
   rid=i['rid']
   print(rid)
   #MiscicSave()
def MiscicSave(rid):
time1=(time.time()*1000)
 url=''
 response=requests.get(url,headers=headers,timeout=3).json()
 misci=response['url']
 try:
     #请求mp3地址，并且进行存储
     content=requests.get(url,headers=headers,timeout=3)
     #文件追加,b进制文件读写
     f=open('./miusc/{}.mp3'.format(name),'ab')
     f.write(content.content)
     f.close
     print(('./miusc/{}.mp3'.format(name),”下载成功！ ！ !“)
  except error as e:
     print(e)
print(time1)

if __name__ == '__main__':
    for page in range(1, 11):
        Index(page)

