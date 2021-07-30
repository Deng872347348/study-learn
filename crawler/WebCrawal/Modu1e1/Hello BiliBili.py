#引入库文件
import  urllib.request
#步骤1，找到要爬取内容的URI
url="https://www.bilibili.com/"
#步骤2，发送HTTP请求
response=urllib.request.urlopen(url)
#步骤3，获取网站响应数据
html=response.content.decode("UTF-8")
with open("U-helloBiliBili.html","w",encoding="UTF-8") as file:
    file.write(html)