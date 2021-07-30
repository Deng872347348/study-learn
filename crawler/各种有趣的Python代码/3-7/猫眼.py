import requests
from fake_useragent import UserAgent
import random
def main():
    url='https://maoyan.com/films'
    headers={
        'User-Agent': str(UserAgent().random)
    }
    resp=requests.get(url,headers=headers).text
    print(resp)
    with open('maoyan.html','w',encoding='UTF-8') as f:
        f.write(resp)