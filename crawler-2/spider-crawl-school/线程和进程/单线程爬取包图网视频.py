import requests
from lxml import etree
import os
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3863.400 QQBrowser/10.8.4334.400',
}
#下载视频的函数
def downmp4(video_url,video_name):
    path='包图网大国工匠视频2'
    #对当前目录下面的文件夹进行判断，如果没有自动创建一个文件夹拉存储
    if not os.path.exists(path):
        os.mkdir(path)
    start_time=time.time()
    video_url="https:"+video_url
    video_name=video_name.strip().replace("<strong>","").replace("</strong>","")
    video_content = requests.get(url=video_url, headers=headers).content
    with open(path+'./%s.mp4'%video_name, "wb") as f:
        f.write(video_content)
    finish_time=time.time()-start_time
    return  "每个视频下载的时间"+str(finish_time)
#数据提取和选择函数
def parsePage():
    # 第一步，确定爬虫地址
    url = "https://ibaotu.com/tupian/gongjiangjingshen/7-0-0-0-0-0-0.html?format_type=0"
    # 第二步：发送请求
    response = requests.get(url=url, headers=headers)
    # 第三步：获取数据
    html_content = response.text
    # 第四部：保存在本地
    # with open('baotuwang.html', 'w',encoding='utf-8') as f:
    #     f.write(html_content)
    #提取a标签
    tree=etree.HTML(html_content)
    video_page_url=tree.xpath("//ul/li/div/div/a/div[1]/video/@src")
    print(video_page_url)
    video_name=tree.xpath("//ul/li/@pr-data-title")
    print(video_name)
    start_time=time.time()
    for i in range(len(video_page_url)):
        downmp4(video_page_url[i],video_name[i])
    finish_time=time.time()
    print("总共下载的时间是"+str(finish_time-start_time))
if __name__ == '__main__':
    parsePage()