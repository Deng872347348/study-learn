import requests
import time
import json
import os


def get_url():
    path = "./image"
    url = 'https://www.toutiao.com/api/search/content'
    headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.82Safari / 537.36'
    }
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': 0,
        'format': 'json',
        'keyword': '车子',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    response = requests.get(url, params=params, headers=headers).json()
    print(response["data"], type(response["data"]))
    if not os.path.exists(path):
        os.mkdir(path)
    for data in response['data']:
        if "url" in data.keys():
            image_url = data["url"]
            # print(data['image_url'])
        else:
            continue
        if "title" in data.keys():
            name = data["title"]
            # print(name)
        else:
            continue
        resp = requests.get(url=image_url, headers=headers)
        with open(path + '.jpg' , 'wb') as f:
            f.write(resp.content)
        # with open("今日头条.txt", 'a', encoding='UTF-8') as fp:
        #     fp.write(name)

if __name__ == '__main__':
    get_url()

