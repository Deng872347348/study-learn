import  requests
url="http://www.daja.net.cn/index.php?m=content&c=index&a=lists&catid=39"
header={
    'Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    'Accept-Encoding":" gzip, deflate'
    'Accept-Language":" zh-CN,zh;q=0.9'
    'Cache-Control":" max-age=0'
    'Connection":" keep-alive'
    'Content-Type":"application/x-www-form-urlencoded'
    'Host":"www.daja.net.cn'
    'Origin":"http://www.daja.net.cn'
    'Referer":"http://www.daja.net.cn/index.php?m=content&c=index&a=lists&catid=39'
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 '

}
title=input("请输入要查找的产品名称: ")
data={
'info[quyu]':  '',
'quyu-1': '',
'quyu-2': ' ' ,
'quyu-3':  ' ' ,
'title':  title,
'company':  ' '
}
response=requests.post(url=url,headers=header,data=data)
print(response.text)
with open("daja.html","w",encoding="utf-8") as fp:
    fp.write(response.text)