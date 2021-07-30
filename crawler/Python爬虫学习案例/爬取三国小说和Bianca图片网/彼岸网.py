import requests
from lxml import etree
import os
import time
import random
path='彼岸明星图片'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
def get_url(page):
    url='http://pic.netbian.com/4kmeinv/index_{}.html'.format(page)
    resp=requests.get(url,headers=headers)
    resp.encoding = 'GBK'
    response=resp.text
    return response
def main(index):
    html=etree.HTML(index)
    img_src = html.xpath('//ul[@class="clearfix"]/li/a/img/@src')
    #print(img_src)
    img_src=['http://pic.netbian.com'+ x for x in img_src]
    img_name=html.xpath('//ul[@class="clearfix"]/li/a/img/@alt')
    #print(img_name)
    for src, name in zip(img_src,img_name):
        img_content=requests.get(src,headers=headers).content
        img_name=name+'.jpg'
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path+'./%s'%img_name,'wb') as f:
            f.write(img_content)
            print("正在下载：",img_name)
    time.sleep(random.randint(1,2))

if __name__ == '__main__':
   ss=str(input('请输入你想要的图片:'))
   a=int(input())
for page in range(1,a):
    index=get_url(page)
    main(index)
