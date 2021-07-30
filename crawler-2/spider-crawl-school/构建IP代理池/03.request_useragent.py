import requests
from  fake_useragent import  UserAgent

url = 'https://www.baidu.com/'
headers = {
    'User-Agent':UserAgent().random}
print(headers)
# 代理ip
proxies = {
    'http': 'http://{}'.format('118.190.95.43'),
    # 'https': 'https://{}'.format('61.135.217.7:80'),
}
print(proxies)

html = requests.get(url=url,headers=headers,proxies=proxies).text

print(html)

"""
免费代理IP http://ip.yqie.com/ipproxy.htm
66免费代理网 http://www.66ip.cn/
89免费代理 http://www.89ip.cn/
无忧代理 http://www.data5u.com/
云代理 http://www.ip3366.net/
快代理 https://www.kuaidaili.com/free/
极速专享代理 http://www.superfastip.com/
HTTP代理IP https://www.xicidaili.com/wt/
小舒代理 http://www.xsdaili.com
西拉免费代理IP http://www.xiladaili.com/
小幻HTTP代理 http://www.feilongip.com/
全网代理IP http://www.goubanjia.com/
飞龙代理IP http://www.feilongip.com/
"""

