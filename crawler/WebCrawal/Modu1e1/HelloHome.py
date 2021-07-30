import  urllib.request
##步骤1，确定要爬取的内容的网址url
url="http://www.huya.com/"
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
}
##步骤2，发出HTTP请求
request=urllib.request.Request(url=url,headers=header)
reponse=urllib.request.urlopen(request)
##步骤3，获取网站响应的数据
content=reponse.read(request)
content=content.decode()
print(content)
##步骤4，对响应的数据进行持久化
with open("huya.html","w",encoding="UTF-8") as fp:
    fp.write(content)