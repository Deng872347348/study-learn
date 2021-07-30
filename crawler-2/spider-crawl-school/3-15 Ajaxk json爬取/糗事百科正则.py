import  requests
import json,time
import re,os

def get_url(page):
    path="./qiutu"
    url="https://www.qiushibaike.com/imgrank/page /{}/".format(page)
    # url="https://www.qiushibaike.com/imgrank/"
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.82Safari / 537.36'
    }
    response=requests.get(url,headers=headers).text
    res='<div class="thumb".*?<img src="(.*?) alt.*?</div>'
    resp = '<div class="content".*?<span>(.*?)</span>.*?</div>'
    picture=re.findall(res,response,re.S)
    title=re.findall(resp,response,re.S)
    # print(title)
    # print(picture)
    if not os.path.exists(path):
        os.mkdir(path)
    for img,title in zip(picture,title):
        img_url="http:"+img
        # title_name=title.strip()
        # # print(title)
        # # print(img_url,title)
        time.sleep(1)
        resp=requests.get(url=img_url,headers=headers).content
        img_name = img_url.split('/')[-1]
        # imgpath = '糗事百科'+img_name
        img_name=img_name.split('.')[0]
        with open(path+'./%s.jpg'%img_name, 'wb') as f:
                f.write(resp)
                print(img_name+"图片下载成功！")
if __name__ == '__main__':
    for i in range(1,13):
          time.sleep(2)
          get_url(i)
