import requests
from lxml import etree
import threading, psutil, os
import time
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3863.400 QQBrowser/10.8.4334.400',
}
def downmp4(item):
    video_url="https://699pic.com/"+item
    video_content = requests.get(url=video_url, headers=headers).text
    tree_video = etree.HTML(video_content)
    video_name = tree_video.xpath("//div[@class='video-view-title clearfix']/h1/text()")[0].replace("\n","").strip() + ".mp4"
    print(video_name)
    xpath_video_src = "https:" + tree_video.xpath("//video/source/@src")[0]
    print(xpath_video_src)
    video_response = requests.get(url=xpath_video_src, headers=headers)
    mp4_content = video_response.content
    with open(video_name, "wb") as f:
        f.write(mp4_content)
def parsePage():
    # 第一步，确定爬虫地址
    url = "https://699pic.com/album/video/0/1142643.html"
    # 第二步：发送请求
    response = requests.get(url=url, headers=headers)
    # 第三步：获取数据
    html_content = response.text.replace("location.href = 'http://' + str;","").replace("fxxkClone();","")
    # 第四部：保存在本地
    with open('shetuwang.html', 'w',encoding='utf-8') as f:
        f.write(html_content)
    #提取a标签
    tree=etree.HTML(html_content)
    video_page=tree.xpath("//ul[@class='clearfix']/li/a[1]/@href")
    print(video_page)
    start_time=time.time()
    ##################线程池的实现方法1###############
    #1.创建线程池，初始化线程数量
    # executor=ThreadPoolExecutor(10)
    # for video_item in video_page[0:5]:
    #     #进入到详情页面下载视频,封装成一个函数----相当于任务
    #     #downmp4(video_item)
    #     executor.submit(downmp4,video_item) #提交任务
    # #关闭线程
    # executor.shutdown()
    ##################线程池的实现方法2###############
    with ThreadPoolExecutor(4) as executor:
        futures=executor.map(downmp4,video_page[0:5])
    for future in futures:
        print(future)
    finish_time=time.time()
    print("总共下载的时间是"+str(finish_time-start_time))
if __name__ == '__main__':
    parsePage()
