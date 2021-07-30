import requests
import jsonpath
import time
import os

url = 'https://tuchong.com/rest/tags/%E7%BE%8E%E5%A5%B3/posts'

num = 10
index = 0

for page in range(1, num + 1):
    time.sleep(5)
    parames = {'page': page, 'count': 20, 'order': 'weekly', 'before_timestamp': ''}
    response = requests.get(url, params=parames).json()

    # print(response)
    img_urls=jsonpath.jsonpath(response,'$..cover_image_src')
    print(img_urls)
    for img_url in img_urls:
        img_content=requests.get(img_url).content
        index+=1
        if not os.path.exists(r'./{}'.format('图虫')):
            os.mkdir(r'./{}'.format('图虫'))
            with open(r'./{}/{}.jpg'.format('图虫',index),'wb') as f:
                f.write(img_content)
                print(r'***正在下载: {}.jpg'.format(index))
