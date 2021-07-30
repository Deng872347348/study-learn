import requests


url='https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

resp=requests.get(url,headers=headers).text
print(resp)