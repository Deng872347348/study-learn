import requests

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',

}

response = requests.get('http://www.duanmeiwen.com/yulu/100653.html', headers=headers,verify=False)
print(response.content.decode("gbk"))