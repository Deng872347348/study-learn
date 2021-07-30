import  requests
import  asyncio
import time
start=time.time()
urls={
'https://blog.csdn.net/weixin_30425949/article/details/97508096','https://www.555vx.com/novel/103648/','https://www.555vx.com/novel/hunzaihougongjiataijian/read_10.html'
}

def get_page(url):
    print("正在下载",url)
    #requests.get是基于同步，必须使用基于异步的网络请求模块进行指定url的请求发送
    #aiohttp:基于异步网络请求的模块
    response=requests.get(url=url)
    print("下载完毕",response.text)

tasks=[]
for url in urls:
    c=get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end=time.time()
print("耗时：",end-start)