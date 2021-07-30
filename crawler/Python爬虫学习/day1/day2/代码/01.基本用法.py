import requests # 需要下载

url = 'https://www.baidu.com/s'


# response1 = requests.get(url)
# print(response1.text)

# 构造请求参数字典 类似formdata
params = {
    "wd": "python"
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'referer': 'https://www.zhihu.com/signin?next=%2F',
    'cookie': '_zap=48721dba-4198-4830-96fd-2739f5e42fd9; d_c0="AJAQypDCaxKPTnuyIkW8xXGAggE2uWbR1KQ=|1609249297"; _xsrf=14101b68-26a1-4194-9b25-7754525fff21; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1611813125,1611824416,1611834671,1611838637; SESSIONID=vxQvV2JJwY72LdUx1IZ4xPNlOC8y0Kc1ag7o7u60VvI; JOID=UVkUCk9wXhNHologCnqbC2w0kk4aBCZKPPNqakgABSR94zl3ctziBC2nWCgPAGMxxqyJI6NI3gWo2U4Vi-GjMag=; osd=U1EUAU5yVhNMo1goCnGaCWQ0mU8YDCZBPfFiakMBByx96Dh1etzpBS-vWCMOAmsxza2LK6ND3weg2UUUiemjOqk=; capsion_ticket="2|1:0|10:1611838643|14:capsion_ticket|44:N2Y4ZjA1NjNlMGQ3NGIzOGEwOGY1MjdlZDJkMGI3YWY=|8054f31b7723c8e04cb35f4c638ca341ca621c415b6a6d8abf084cc15722a337"; z_c0="2|1:0|10:1611838702|4:z_c0|92:Mi4xbmptbklRQUFBQUFBa0JES2tNSnJFaVlBQUFCZ0FsVk43Z0lBWVFDdnJLbERoWnpjQXNnbE1lN2V6UVFmU0VLVWxn|87067f009721287ce7f3b11547b0f8954b5b28340096226d69d237df8238fedc"; unlock_ticket="ACBbC46lSBImAAAAYAJVTfa7EmDIa2a0PIKZQjgWGSf4hTJxcfxVPw=="; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1611838705; KLBRSID=c450def82e5863a200934bb67541d696|1611838723|1611838636'
}

response2 = requests.get(url,headers=headers,params=params)

# 文本内容
print(response2.url) # 解决中文乱码
with open('baidu2.html','wb')as f:
    f.write(response2.content)
# 响应状态
# print(response.status_code)

# 查看响应头
# print(response.headers)

# 查看请求头
# print(response.request.headers)