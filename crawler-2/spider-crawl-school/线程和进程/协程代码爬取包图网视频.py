import requests
from lxml import etree
import threading, psutil, os
import time
from concurrent.futures import ThreadPoolExecutor
import  asyncio
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3863.400 QQBrowser/10.8.4334.400',
}
def downmp4(video_url,video_name):
    #开启线程
    thread=threading.current_thread()
    process=psutil.Process(os.getpid())
    print(thread.ident,thread.name,process.pid,process.name())
    start_time=time.time()
    video_url='http:'+video_url
    #对视频的地址进行详细请求
    video_name = video_name.strip().replace('<strong>', '').replace('</strong>>', '')
    print(video_name)
    resp=requests.get(ulrl=video_url,headers=headers).content
    with open(video_name+'.mp4','wb') as f:
        f.write(resp)
    finishTime=time.time()-start_time
    # print("进程执行的时间%d"%(finishTime))
    return video_name+".mp4","finishTime:",finishTime
#定义线程函数
def call_back(res):
        #完成线程的操作，进行回调的函数
        res=res.result()#获取结果
        print(res)
def parsePage():
    # 第一步，确定爬虫地址
    url = "https://ibaotu.com/tupian/gongjiangjingshen/7-0-0-0-0-0-0.html?format_type=0"
    # 第二步：发送请求
    response = requests.get(url=url, headers=headers)
    # 第三步：获取数据
    # html_content = response.text.replace("location.href = 'http://' + str;","").replace("fxxkClone();","")
    html_content=response.text
    # 第四部：保存在本地
    with open('baotuwang.html', 'w',encoding='utf-8') as f:
        f.write(html_content)
    tree=etree.HTML(html_content)
    #提取a标签
    video_name = tree.xpath("//ul/li/div/div/a/div[2]/img/@alt")
    print(video_name)
    video_url=tree.xpath("//ul/li/div/div/a/div[2]/img/@src")
    print(video_url)
    start_time=time.time()
    ##################线程池的实现方法2###############
    # executor = ThreadPoolExecutor(4)
    # for i in range(len(video_url)):
    #     # 进入到详情页面下载视频,封装成一个函数----相当于任务
    #     # downmp4(video_item)
    #     executor.submit(downmp4, video_url[i], video_name[i]) .add_done_callback(call_back()) # 提交任务
    # # 关闭线程
    # executor.shutdown(True)
    # finishTime=time.time()-start_time
    # print("Total finishTime:",finishTime)

    #创建协程任务
    loop=asyncio.get_event_loop()
    downMP4Task=[]
    for i in range(len(video_url)):
        downMP4Task=downmp4(video_url[i],video_name[i])
        future=asyncio.ensure_future(downMP4Task)
        #打印协程状态
        print(future)
        downMP4Task.append(future)
    loop.run_until_complete(asyncio.wait(downMP4Task))
    loop.close()
    finishTime=time.time()-start_time
    print("Total finishTime:",finishTime)
if __name__ == '__main__':
    parsePage()
