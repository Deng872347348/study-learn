import  urllib.request
#步骤1，确定我们要爬取内容的url
url="https://vip.iqiyi.com/"
#增加U-A伪装请求头
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
}
# #步骤2，发送HTTP请求
#包括请求头设置的请求
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
#步骤3，获取网站的响应的数据
content=response.read()
content=content.decode()
#步骤4，对响应的数据进行持久化
print(content)
with open("yip.html","w",encoding="UTF-8") as fp:
    fp.write(content)
