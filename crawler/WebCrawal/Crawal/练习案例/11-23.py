#环境安装：pip install aiohttp
import  requests
import  asyncio
import time
import  aiohttp

start=time.time()
urls={
'https://blog.csdn.net/weixin_30425949/article/details/97508096','https://www.555vx.com/novel/103648/','https://www.555vx.com/novel/hunzaihougongjiataijian/read_10.html'
}

async def get_page(url):
    async  with aiohttp.ClientSession() as session:
        #get(),post()
        #headers,params/data,proxy='http://ip:port'
        async  with session.get(url) as response:
            #text()返回字符串形式的响应数据
            #read()返回的二进制形式的响应数据
             #json()返回的就是json对象
            #注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text= await  response.text()
            print(page_text)
# def get_page(url):
#     print("正在下载",url)
#     #requests.get是基于同步，必须使用基于异步的网络请求模块进行指定url的请求发送
#     #aiohttp:基于异步网络请求的模块
#     response=requests.get(url=url)
#     print("下载完毕",response.text)

tasks=[]
for url in urls:
    c=get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end=time.time()
print("耗时：",end-start)