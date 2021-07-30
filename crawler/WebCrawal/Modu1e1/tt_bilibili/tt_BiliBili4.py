#引入库文件
import  requests
#步骤1，找到要爬取的url
url="https://www.youku.com/"
#确定要搜索的关键字
wd=input("请输入搜索的关键字：")
#设置url的额外参数
param={
    "wd":wd
}
#构造请求头
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
}
#步骤2，发送HTTP请求
response=requests.get(url,params=param,headers=header)
#步骤3 ，获取网站响应的数据
html=response.text
#步骤4，对获取的响应的数据进行持久化
with open("R-helloyouku.html.html.html","w",encoding="UTF-8") as file:
    file.write(html)



