import requests
import re
from fake_useragent import  UserAgent
headers= {'User-Agent':str(UserAgent().random)}
# obj=re.compile(r"url: '(?P<url>.*?)',",re.S)
# url="https://www.91kanju.com/vod-play/58681-1-1.html"
# resp=requests.get(url)
# # print(resp.text)
#
# m3u8_url=obj.search(resp.text).group("url")#拿到m3u8的地址
#
# print(m3u8_url)
#
# #下载m3u8文件
# response=requests.get(m3u8_url,headers=headers)
#
# with open("猎鹰与冬兵.m3u8",mode='wb') as f:
#     f.write(response.content)
#     f.close()
#     print("下载完成")


#读取下载的m3u8文件
n=1
with open("猎鹰与冬兵.m3u8",mode='r',encoding='utf-8') as f:
    for line in f:
        line=line.strip() #先去掉空格，空白，换行符
        if line.startswith('#'):
            continue
        resp3=requests.get(line)
        f=open(f'video/{n}.ts',mode='wb')
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1
        print("完成{}".format(n))