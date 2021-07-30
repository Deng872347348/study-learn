import requests
from pyquery import PyQuery as pq

headers = {
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.104Safari / 537.36'
}
count = 1

# 封装一个函数，里面主要定义request.get请求
def RequestIndex(page):
    url = 'https://www.buxiuse.com/?page={}'.format(page)

    response = requests.get(url, headers=headers).text
    #print(response)


# 提取数据
def dataEX(index):
    doc=pq(index)
    height_main = doc('.height_main').item()
    for i in height_main:
        print(i)
        imgUrl = (i.attr('scr'))
        print(imgUrl)


# 保存图片，数据的持久化

def ImgSave(imgUrl):
    global count
    respon = requests.get(imgUrl, headers=headers)
    with open('./不羞色社区小姐姐们/{}.jpg'.format(count), 'wb') as f:
        f.write(respon.content)
        count += 1


if __name__ == '__main__':
    for page in range(1, 10):
        index = RequestIndex(page)
        dataEX(index)

