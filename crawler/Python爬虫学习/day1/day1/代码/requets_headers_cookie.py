# cookie字段是用来做用户访问状态的保持
import requests
import re

def login():
    """
    Url
    session
     headers
     发送请求获取响应
    """
    session = requests.session()
    session.headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    url1 = 'https://github.com/login'
    res_1 = session.get(url1).content.decode()
    # url_1 获取token
    token = re.findall('name="authenticity_token" value="(.*?)" />',res_1)[0]
    print(token)


    # url2 -登录
    url2 = 'https://github.com/session'

    formdata = {
            "commit": "Sign in",
            "authenticity_token": token,
            "login": "2814632150@qq.com",
            "password": "jiuge@123",
            "webauthn-support": "supported"
    }

    print(formdata)
    session.post(url2,data=formdata)

    # url3 验证
    url3 = 'https://github.com/jiuge123223332'
    response = session.get(url3)
    with open('github.html','wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    login()

# put  updata 添加
# delete 删除
# header # 头
# options