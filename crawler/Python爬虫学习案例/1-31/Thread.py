#多线程爬取壁纸
import requests
from lxml import etree
import  threading
headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.104Safari / 537.36'
    }
# def get_data(url):
#     resp=requests.get(url,headers=headers)
#     #提取数据
#     data=etree.HTML(resp.text)
#     print(resp.text)
#     # picture_url=data.xpath('//img/@data-progressive')
#     # picture_name=data.xpath('//h3/text()')
#     #
#     # for name,img_url in zip(picture_name,picture_url):
#     #       img_url=img_url.spilt('_')[0]+'_'++img_url.spilt('_')[1]
#     #       print(img_url)
#     #       result=requests.get(img_url,headers=headers).content
#     #       name=name.split()[0]+'.jpg'
# def main():
#     down_yema=input('请输入你要获取的页数消息:')
#     for i in range(1,int(down_yema)+1):
#        url='https://bing.ioliu.cn/?p={}'.format(i)
#        get_data(url)
#        t=threading.Thread(target=get_data,args=(url,))
#        t.start()
# if __name__ == '__main__':
#     main()

# url='https://bing.ioliu.cn/?p=1'
# resp=requests.get(url,headers=headers)
# print(resp.text)
