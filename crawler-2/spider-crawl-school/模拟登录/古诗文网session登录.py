import requests


url='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fshiwens%2fdefault.aspx'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

data={
'__VIEWSTATE':'CWD3mDcaisXo67Ny6m9494a9lPGEpHUGU0eOcFrmWXifAX9pTFAIYY7jw3DofpBn1R+J6sngq+Rk5SEkBdMmhK/Wv0z7M7mHj+uDllXFSnnPOKsOsQ6wWdA46yQ=',
'__VIEWSTATEGENERATOR': 'C93BE1AE',
'from': 'http://so.gushiwen.cn/shiwens/default.aspx',
'email': '15608471682',
'pwd': '15608471682.a',
'code': 'zzbc',
'denglu': '登录',
}
#建立请求session对象
session=requests.session()

response=session.post(url=url,headers=headers,data=data)

response.encoding=response.apparent_encoding

#提取响应数据
html_content=response.text
print(response.status_code)

with open('hellorenrenwang.html','w',encoding='utf-8') as fp:
    fp.write(html_content)

