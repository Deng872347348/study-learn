import requests
import re
import os

if not os.path.exists("./img"):
    os.mkdir("./img")

url = "https://www.qiushibaike.com/imgrank/"

header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0 Safari/537.36"
}

html = requests.get(url=url,headers=header).content.decode("utf-8")
res = '<div class="thumb".*?<img src="(.*?) alt.*?</div>'
resp = '<div class="content".*?<span>(.*?)</span>.*?</div>'
picture = re.findall(res, html, re.S)
title = re.findall(resp, html, re.S)
a =[]
for p in picture:
    a.append("https:"+str(p).replace('"',""))
for b in a :
    img = requests.get(url=b,headers=header).content
    imagename = b.split("/")[-1]
    with open("./img/" + imagename, "wb")as f:
        f.write(img)
        print(imagename)
