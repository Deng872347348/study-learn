import requests
from lxml import etree
url='https://ibaotu.com/shipin/7-0-0-0-0-1.html'
response=requests.get(url)#发送请求
#print(response)

#对于得到的
html_text=response.content.decode()

html=etree.HTML(html_text)

path='E:\python社区版\python项目\Python小案例\腾讯课堂爬虫学习案例\pic'

video_urls=html.xpath('//div[@class="video-play"]/video')
video_names=html.xpath('//span[@class="video-title"]/text()')
for video_urls,video_names in  zip(video_urls,video_names):

    video_urls='http:'+video_urls
    video_urls=video_urls.replace(".mp4","")
    video_data=requests.get(video_urls).content

    with open(path+video_names+".mp4",'wb') as f:
        f.write(video_data)
        print(video_names+'....'+"视频爬取完毕")