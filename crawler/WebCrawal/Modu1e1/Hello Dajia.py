import  requests
url="http://www.daja.net.cn/html/2017/yaowen_1019/452"
header={
'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection':' keep-alive',
'Host': 'www.daja.net.cn',
'Referer': 'http://www.daja.net.cn/',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}
data={
    'info[quyu]':'20',
     'quyu-1':'20',
    'quyu-2':'',  
     'quyu-3':'',
    'title':'酒'
      'compay': ''
}
response=requests.post(url=url,headers=header,data=data)
print(response.text)