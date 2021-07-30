from multiprocessing.dummy  import Pool
import requests
import time
import asyncio




async def get_request(url):
    print('正在请求url', url)
    time.sleep(2)
    print('请求结束', url)
    return 'bobo'


urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com'
]

if __name__ == '__main__':
    start=time.time()
    tasks=[]#多任务列表
   #创建协程对象
    for url in urls:
        c=get_request(url)
        #创建任务对象
        task=asyncio.ensure_future(c)
        tasks.append(task)
     #创建事件循环对象
        loop=asyncio.get_event_loop()
        # loop.run_until_complete(tasks)
        loop.run_until_complete(asyncio.wait(tasks))
        print("总耗时：",time.time()-start)