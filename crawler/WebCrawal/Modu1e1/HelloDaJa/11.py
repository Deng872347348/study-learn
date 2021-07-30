import requests
from bs4 import BeautifulSoup
url = "https://www.bilibili.com/"
header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'
    }
response = requests.get(url,headers=header)
html = response.content.decode("utf-8")

soup = BeautifulSoup(html,'lxml')
sq = soup.select('a')

for zd in sq:
    print(zd.attrs)
