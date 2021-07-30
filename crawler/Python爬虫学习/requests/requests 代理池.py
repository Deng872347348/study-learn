import requests

url='http://www.baidu.com'

proxy={

}
response=requests.get(url,proxies=proxy)

print(response)