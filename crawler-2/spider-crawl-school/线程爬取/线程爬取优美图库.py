import asyncio
import aiohttp


urls={
    'http://kr.shanghai-jiuxin.com/file/mm/20210503/1htg5x3zaf2.jpg',
     'http://kr.shanghai-jiuxin.com/file/mm/20210503/fo32lx22jui.jpg',
     'http://kr.shanghai-jiuxin.com/file/mm/20210503/yks1kolmp42.jpg'
}
async  def aiodownload(url):
    name=url.rsplit("/",1)[1]#
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #请求回来了，写入文件
            with open(name,mode="wb") as f:
                f.write(await resp.content.read())#读取内容是异步的，需求await挂起
    print(name,"搞定")
    #s=aiohttp.ClientSession() <==> requests
    #requests.get() .post()
    #s.get() .post()
    #发送请求
    #得到图片内容
    #保存文件

async def main():
    tasks=[]
    for url in urls:
        tasks.append(aiodownload(url))
        await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())