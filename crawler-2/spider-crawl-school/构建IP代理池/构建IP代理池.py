import requests
from bs4 import BeautifulSoup
import time
import pickle as pickle
import os
def get_html(url, flag=True):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if flag:
            response.encoding = 'utf-8'
        else:
            response.encoding = 'gb2312'
        return response.text
    except Exception as err:
        return '请求异常'
def get_66ip():
    ip_list = []
    for index in range(1, 35):
        count = 0
        province = ''
        url = 'http://www.66ip.cn/areaindex_{}/1.html'.format(index)
        html = get_html(url, flag=False)
        soup = BeautifulSoup(html, 'lxml')
        tr_list = soup.find_all(name='tr')
        for tr_ in tr_list[2:]:
            td_list = tr_.find_all(name='td')
            ip = td_list[0].string
            port = td_list[1].string
            province = td_list[2].string
            ip_port = ip + ':' + port
            ip_list.append(ip_port)
            count += 1
        print('Saved {0} {1} ip.'.format(province, count))
        # 速度不要太快哦!, 否则获取不到页面内容
        time.sleep(3)
    # path='66ip.pickle'
    # if not os.path.exists(path):
    #     os.mkdir(path)
    with open('66ip.pickle.txt', 'wb') as f:
        pickle.dump(ip_list, f)
    print('Finished!!!')
    print(ip_list)
if __name__ == '__main__':
    get_66ip()