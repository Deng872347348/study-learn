import time

import requests

import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.66 Safari/537.36'
}
response = requests.get('http://www.jituwang.com/tuku/', headers=headers)

# print(requests.request.headers)
# print(requests.text)

html = response.text

dir_name = re.findall('<h3>(.*?)</h3>', html)[-1]

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall(' <a  href="(.*?)" class="list3Pad"><div class="anPic"><img src=".*?" alt=".*?"/></div>', html)

url_list = []
for i in urls:
    url_list.append(i.replace('//', 'http://'))

for url in url_list:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    with open(file_name, 'wb')as f:
        f.write(response.content)