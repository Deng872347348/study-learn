import  requests_test

url = 'http://www.baidu.com'

proxy = {
    'HTTP':'http://49.86.26.63:9999',
    'TTTP':'http://39.64.95.65:8118',
}

proxy = {
    'http':'http://user:pwd@49.86.26.63:9999',
    'HTTPS':'https://user:pwd@49.70.99.204:9999',
}

response = requests_test.get(url, proxies = proxy)
print(response)