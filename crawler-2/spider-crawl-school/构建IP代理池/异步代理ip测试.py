
import requests
from bs4 import BeautifulSoup
import time
import pickle as pickle
import  aiohttp
import asyncio
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
    return ip_list
    # path='66ip.pickle'
    # if not os.path.exists(path):
    #     os.mkdir(path)
    # with open('66ip.pickle.txt', 'wb') as f:
    #     pickle.dump(ip_list, f)
    # print('Finished!!!')
    # print(ip_list)
async def test_ip(ip_, url):
    global ip_ok
    conn = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            proxy_ip = 'http://' + ip_
            print('正在测试: ' + proxy_ip)
            async with session.get(url=url, headers=headers, proxy=proxy_ip, timeout=15) as response:
                if response.status == 200:
                    print('代理可用: ' + ip_)
                    ip_ok.append(ip_)
                else:
                    print('请求响应码不合法 ' + ip_)
        except:
            print('代理请求失败', ip_)
if __name__ == '__main__':
    url = 'https://blog.csdn.net/Deng872347348/article/details/117004434'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    ip_list=get_66ip()
    # get_kaixinip()
    # get_goubanjiaip()
    # get_kuaidaili()
    with open('66ip.pickle.txt', 'rb') as f1:
        ip_list1 = pickle.load(f1)
        ip_list1 = list(set(ip_list1))
    # with open('./ip/kaixinip.pickle', 'rb') as f2:
    #     ip_list2 = pickle.load(f2)
    #     ip_list2 = list(set(ip_list2))
    # with open('./ip/goubanjiaip.pickle', 'rb') as f3:
    #     ip_list3 = pickle.load(f3)
    #     ip_list3 = list(set(ip_list3))
    # with open('./ip/kuaidaili.pickle', 'rb') as f4:
    #     ip_list4 = pickle.load(f4)
    # ip_list = ip_list1 + ip_list2 + ip_list3 + ip_list4
    ip_ok = []
    print('开始测试: ')
    try:
        loop = asyncio.get_event_loop()
        for i in range(0, len(ip_list), 10):
            proxies_ip = ip_list[i: i + 10]
            tasks = [test_ip(proxy_ip, url) for proxy_ip in proxies_ip]
            loop.run_until_complete(asyncio.wait(tasks))
            time.sleep(5)
    except Exception as err:
        print('发生错误:', err.args)

    with open('all_ip_ok.pickle.txt', 'wb') as f_:
        pickle.dump(ip_ok, f_)
    print(ip_ok)

