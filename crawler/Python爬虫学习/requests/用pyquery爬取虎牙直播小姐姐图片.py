#第一步，导入包
import  requests
import os
from pyquery import  PyQuery as pq
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
def RequestIndex():

    url='https://www.huya.com/g/2168'
    response=requests.get(url,headers=headers).text
    return response

#数据的一个提取
def dataEx(index):
    doc=pq(index)#把提取到得整个页面传进去
    image=doc('.pic').items()
    #print(image)
    for li in image:
        imgUrl=(li.attr('data-original'))
        name=(li.attr('title'))
        imgUrl=imgUrl.split('?')[0]
        Imagesave(imgUrl,name)
        #print(name)
def Imagesave(imgUrl,name):
    path='虎牙小姐姐'
    if not os.path.exists(path):
        os.mkdir(path)
    image_url=requests.get(imgUrl,headers=headers)
    #print(image_url)
    with open(path+'./%s.jpg'%name,'wb') as f:
        f.write(image_url.content)
        print(name+'下载成功')
if __name__ == '__main__':
    index=RequestIndex()
    dataEx(index)