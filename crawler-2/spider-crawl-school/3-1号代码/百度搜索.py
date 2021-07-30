import requests # 需要下载
wd=input('请输入关键词:')
url = 'https://uland.taobao.com/sem'
# response1 = requests.get(url)
# print(response1.text)
# 构造请求参数字典 类似formdata
params = {
    "keyword": wd
}
# proxy = {
#     'HTTP':'http://49.86.26.63:9999',
#     'TTTP':'http://39.64.95.65:8118',
#     'http':'http://user:pwd@49.86.26.63:9999',
#     'HTTPS':'https://user:pwd@49.70.99.204:9999',
# }

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

response = requests.get(url,headers=headers,params=params)

# 文本内容
# print(response.url) # 解决中文乱码
response=response.content.decode('UTF-8')
# response=response.text
with open('淘宝.html','w',encoding='UTF-8')as f:
    f.write(response)