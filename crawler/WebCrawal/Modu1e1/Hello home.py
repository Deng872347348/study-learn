import urllib.request
##步骤1，确定要爬取的内容的网址url
url="https://www.douban.com/"
##步骤2，发出HTTP请求
response=urllib.request.urlopen(url)
##步骤3，获取网站响应的数据
content=response.read()
content=content.decode()
##步骤4，对响应的数据进行持久化
print(content)
with open("douban.html","w",encoding="UTF-8") as fp:
    fp.write(content)
