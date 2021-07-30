import requests
from lxml import etree
import threading, psutil, os
import time
import threading,psutil,os
from concurrent.futures import  ThreadPoolExecutor,ProcessPoolExecutor
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3863.400 QQBrowser/10.8.4334.400',
}
def downmp4(item):  #下载单个mp4的视频
     video_page_url="https://699pic.com/"+item
     video_page_response = requests.get(url=video_page_url, headers=headers)
     video_page_content= video_page_response.text
     tree_video = etree.HTML(video_page_content)
     video_name = tree_video.xpath("//div[@class='video-view-title clearfix']/h1/text()")[0].replace("\n","").strip() + ".mp4"
     print(video_name)

     # 开启进程
     thread = threading.current_thread()
     process = psutil.Process(os.getpid())
     print("当前线程名称:%s,ID:%s,所在的进程名称%s:进程ID：%s" %
           (thread.getName(), thread.ident, process.pid, process.name()))

     xpath_video_src = "https:" + tree_video.xpath("//video/source/@src")[0]
     print(xpath_video_src)
     video_response = requests.get(url=xpath_video_src, headers=headers)
     mp4_content = video_response.content
     with open(video_name, "wb") as f:
         f.write(mp4_content)
#定义线程函数
def call_back(res):
        #完成线程的操作，进行回调的函数
        res=res.result()#获取结果
        # print(res)
def parsePage():
    # 第一步，确定爬虫地址
    url = "https://699pic.com/album/video/0/1142643.html"
    # 第二步：发送请求
    response = requests.get(url=url, headers=headers)
    # 第三步：获取数据
    html_content = response.text.replace("location.href = 'http://' + str;","").replace(" fxxkClone();","")
    # print(html_content)
    # 第四部：保存在本地
    # with open('shetuwang.html', 'w',encoding='utf-8') as f:
    #     f.write(html_content)
    #提取页面中a标签中的链接
    tree=etree.HTML(html_content)
    print(tree)
    xpath_video_page=tree.xpath("//ul[@class='clearfix']/li/a[1]/@href")
    # print(xpath_video_page)
    item_list=xpath_video_page[0:5]
    print(item_list)
    start_time=time.time()
    # for video_item in xpath_video_page[0:5]:  #进入到下载视频的详情页面
    #     #调用下载视频的函数
    #     downmp4(video_item)
    ##################线程操作方式1####
    executor = ThreadPoolExecutor(max_workers=4)
    for item in item_list:
        executor= executor.submit(downmp4, item).add_done_callback(call_back)
    executor.shutdown(True)
     #####################
    ##################线程操作方式2####
    # with ThreadPoolExecutor(max_workers=4) as executor
    #       futures=executor.map(downmp4(),item_list)
    # for future in futures:
    #     print(future)
    #####################
    ##################进程操作方式####
    # executor=ProcessLookupError(max_workers=4)
    # for item in item_list:
    #     futures=executor.submit(downmp4, item).add_done_callback(call_back)
    #  executor.shutdown(True)
    #####################
    print("总共用时为:%s second"+(time.time()-start_time))
if __name__ == '__main__':
    parsePage()


