import  requests

url='https://www.baidu.com'
response=requests.get(url)
print(response.cookies)

for key,value in response.cookies.items():
    print(key+'='+value)
