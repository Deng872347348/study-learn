# 引入库文件
import  requests
import  re
# 找到要爬取的URL
url="http://www.rednet.cn/"
# 构造U-A伪请求头
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
# 发送HTTP请求
response=requests.get(url,headers=header)
# 获取响应数据
html=response.content.decode("UTF-8")
# 获取<title></title>标题
# 分析内容的结构
# 构建数据解析对象
pattern1=re.compile(r'<title>(.*?)</title>')
# 对数据进行解析
title=pattern1.findall(html)
# 获取解析的数据
print("title标题：")
print(title)
# print("a标签的内容:")
# for value in a_content:
#     print(value)
# 获取<a></a>标签的内容
# 分析内容结构
# 构建解析对象
pattern2=r'<a .*?>(.*？)</a>'
# 对数据进行解析
a_content=re.findall(pattern2,html,re.S|re.M)
# 获取解析数据
print("a标签的内容：")
for value in a_content:
    print(value)