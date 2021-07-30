import requests
import time
import json

url = 'https://movie.douban.com/j/search_subjects'
headers = {
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.190Safari / 537.36',
}
params = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': '20',
    'page_start': '20'
}
resp = requests.get(url=url, params=params, headers=headers)
# resp = resp.encoding('GBK')
movie_list = resp.json()
with open('doubanmovie.json', 'w') as fp:
    json.dump(movie_list, fp)
for movie in movie_list['subjects']:
    name = movie['title']
    rate = movie['rate']
    cover_url = movie['cover']
    print(name, rate, cover_url)
    # 级联操作
    response_cover = requests.get(url=cover_url, headers=headers)

    cover_data = response_cover.content
    cover_file = rate + name + ".jpg"
    with open(cover_file, 'wb') as fp:
        fp.write(cover_data)
