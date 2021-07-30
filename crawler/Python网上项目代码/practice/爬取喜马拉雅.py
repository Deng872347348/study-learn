import requests

url="https://www.ximalaya.com/revision/play/v1/audio?id=178084159&ptype=1"

headers={

}
response=requests.get(url,headers=headers).json()
data=response['data']['src']#有声小说的下载地址
name=data.split('/')[7]#忘记的名称
mp3=requests.get(data,headers=headers)
f=open('./m4a/'+name,'ab')#文件的路径,文件写入方式 a 文件追加(不存在新建)b 进制文件
f.write(mp3.content)
f.close()

url="https://www.ximalaya.com/youshengshu/mr132t27722"
response=requests.get(url,headers=headers).text
doc=pq(response) #pyquery 对象初始化
cover=doc('.album-cover.corner-prefer-mark.lg.neednover.ig').item()
for i in cover:
     album='https:www.ximalaya.com'+str(i.attr('href'))
     # print(album)
     main(album)
def main(urls):
    response=requests.get(urls,headers=headers).text
    doc=pq(response)
    text1=doc(".text.lF_ a").items()
    # print(text1)
    for i in text1:
        id1=i.attr('href').split('/')[3]
        print(id1)
if __name__ == '__main__':
    Parsel()
