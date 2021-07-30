'''''
思路：
1.拿到主页面的页面源代码，找到iframe
2从iframe的页面源代码中拿到m3u8文件
3下载第一层m3u8文件-,下载第二层m3u8文件(视频存储路径)
4,下载视频
5下载密钥，进行解密操作
6 合成ts文件成为一个mp4文件
'''
import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
import asyncio
import aiohttp
import aiofiles
import os
from  Crypto.Cipher import AES
headers= {'User-Agent':str(UserAgent().random)}
def get_iframe_src(url):
    # resp=requests.get(url)
    # html_page=BeautifulSoup(resp.text,'html.parser')
    # src=html_page.find('iframe').get('src')
    # print(src)
    # return src
    return  'https://www.1717yun.com/jx/ty.php?url=http://tv.sohu.com/20130914/n386591910.shtml'#为了测试
def get_first_m3u8_url(url):
    resp=requests.get(url)
    print(resp.text)
    # obj=re.compile(r'var main="(?P<m3u8_url>.*?)"',re.S)
    # m3u8_url = obj.search(resp.text).group("m3u8_url")  # 拿到m3u8的地址
    # print(m3u8_url)
    # return m3u8_url

def download_m3u8_url(url,name):
    response=requests.get(url)
    with open(name, mode='wb') as f:
        f.write(response.content)
        f.close()
        # print("下载完成")

async  def download_ts(url,name,session):
   async with session.get(url) as resp:
       async with aiofiles.open(f'video2/{name}',mode='wb') as f:
         await f.write(await resp.content.read())#把下载别的内容写入到文件中
       print(f'{name}下载完毕')
#定义异步协程函数
async  def aio_download(up_url):
    task=[]
    async  with aiohttp.ClientSession() as session:#提前准备号session
       async with aiofiles.open("下载的视频名称.txt",mode='r',encoding='utf-8') as f:
          async for line in f:
                if line.startswith("#"):
                    continue
                line=line.strip()#去掉换行
                #拼接真正的ts路径
                ts_url=up_url+line
                task=asyncio.create_task(download_ts(ts_url,line))
                task.append(task)
          await  asyncio.wait(task)
#定义下载密钥的函数
def get_key(url):
    resp=requests.get(url)
    print(resp.text)
async  def dec_ts(name,key):
    aes=AES.new(key=key,IV=b'0000000000000000',mode=AES.MODE_CBC)
    async  with aiofiles.open(f'video2/{name}',mode='rb') as f1,\
        aiofiles.open(f'video2/temp_{name}',mode='wb') as f2:
        bs=await  f1.read() #从源文件读取内容
        await  f2.write(aes.decrypt(bs))#把解密好的内容写入到文件
    print(f'{name}解密完成')
async def aio_dec(key):#定义解密函数
   tasks=[]
   async with aiofiles.open("下载的视频名称.txt",mode='r',encoding='utf-8') as f:
     async for line in f:
         if line.startswith("#"):
             continue
         line = line.strip()  # 去掉换行
         # 开始解密创建多任务
         task = asyncio.create_task(dec_ts(line, key))
         tasks.append(task)
     await  asyncio.wait(tasks)
#定义函数。进行ts合并成mp4视频
def merge_ts():
    lst=[]
    with aiofiles.open("下载的视频名称.txt", mode='r', encoding='utf-8') as f:
      for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()  # 去掉换行
            lst.append(f'vdeo2/temp_{line}')
    s=" ".join(lst)
    os.system(f'cat {s} > movie.mp4')
    print('完成')
def main(url):
    #拿到主页面的源代码，找到iframe的src入口
    ifrmae_src=get_iframe_src(url)
    get_first_m3u8_url(ifrmae_src)
    #拿到第一层的m3u8文件地址
    first_m3u8_url=get_first_m3u8_url(url)
    #拿到iframe的域名
    ifram_domin=ifrmae_src.split("/share")[0]
    #拼接出真正德m3u8文件地址
    first_m3u8_url=ifram_domin+first_m3u8_url
    #下载第一层m3u8文件
    download_m3u8_url(first_m3u8_url)#第一层m3u8文件
    #读取下载的第一层的m3u8文件
    with open("猎鹰与冬兵.m3u8", mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line=line.strip()#
                #准备拼接第二成m3u8地址
                second_m3u8_url=first_m3u8_url.split("index.m3u8")[0]+line
                #下载第二层的m3u8
                download_m3u8_url(second_m3u8_url,"下载视频的名称")
    #替换，拿到真实的ts的路径，地址，下载并且请求
    second_m3u8_up_url=second_m3u8_url.replace('index.m3u8','')
    #异步协程
    asyncio.run(aio_download(second_m3u8_up_url))
    #拿到密钥
    key_url=second_m3u8_up_url+'key.key'#偷懒写入，正常情况下我们应该到m3u8文件里面去找
    key=get_key(key_url)
    #解密操作
    asyncio.run(aio_dec(key))

    #合并所有的ts为mp4
    merge_ts()
if __name__ == '__main__':
    url="https://www.91kanju.com/vod-play/541-2-1.html"
    main(url)
