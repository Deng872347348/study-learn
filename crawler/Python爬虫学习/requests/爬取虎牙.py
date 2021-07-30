import requests
from lxml import etree
import time
import os

url = 'https://www.huya.com/g/2168'


def get(url):
    response = requests.get(url)
    html = etree.HTML(response.text)
    girls = html.xpath('//img[@class="pic"]')
    # print(girls)
    path = '虎牙小姐姐/'
    if not os.path.exists(path):
        os.mkdir(path)
    for girl in girls:
        img_url = girl.xpath('./@data-original')[0]
        img_url = img_url.split('?')[0]
        name = girl.xpath('./@alt')[0]
        # img_url=girl.xpath('./@src')[0]
        # print(img_url)
        image = requests.get(img_url)
        # print(img_url)
        # time.sleep(1)
        # print(name)
        time.sleep(1)
        with open(path + '%s.jpg' % name, 'wb') as f:
            f.write(image.content)
            print('正在下载', name)


if __name__ == '__main__':
    get(url)
