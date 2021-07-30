import os
import requests
from bs4 import BeautifulSoup

if not os.path.exists('./images/'):
    os.mkdir('./images/')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

url = 'https://fabiaoqing.com/biaoqing/lists/page/1.html'
response = requests.get(url, headers=headers).text

'''
lxml: html解析库,因为python和html两者没有关系
python没有办法直接控制html代码
我们就需要使用lxml这个库将html代码转成python对象
    需要大家去下载 pip install lxml
'''
soup = BeautifulSoup(response, 'lxml')
img_list = soup.find_all('img', class_='ui image lazy')
for img in img_list:
    img_url = img['data-original']
    img_title = img['title']
    print(img_url, img_title)

    try:
        with open('./images/' + img_title + os.path.splitext(img_url)[-1], 'wb') as f:
            '''
        因为一张图片是二进制数据
            如果我们使用text文本形式返回
            会对文件造成破坏

            使用content去返回原始数据

        '''
            image = requests.get(img_url, headers=headers).content
            # 写入二进制数据 image这个变量是存储requests返回的二进制数据的
            f.write(image)
            print('保存成功:', img_title)
    except:
      pass
