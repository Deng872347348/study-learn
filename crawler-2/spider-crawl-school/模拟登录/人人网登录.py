import requests
if __name__ == "__main__":

    #登录请求的url（通过抓包工具获取）
    post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021411021451'
    #创建一个session对象，该对象会自动将请求中的cookie进行存储和携带
    session = requests.session()
   #伪装UA
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    formdata = {
        'email': '15608471682',
        'icode': '',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '2f8da46a49af8268e937720f06cc5e3152ba01c97825fdece839ad83a6697ce1',
        'rkey': 'd0cf42c2d3d337f9e5d14083f2d52cb2',
        'f': 'http%3A%2F%2Fwww.renren.com%2F976856991%2Fnewsfeed%2Fphoto',
    }
    #使用session发送请求，目的是为了将session保存该次请求中的cookie
    session.post(url=post_url,data=formdata,headers=headers)

    get_url = 'http://www.renren.com/960481378/profile'
    #再次使用session进行请求的发送，该次请求中已经携带了cookie
    response = session.get(url=get_url,headers=headers)
    #设置响应内容的编码格式
    response.encoding =response.apparent_encoding
    #将响应内容写入文件
    with open('./renren.html','w',encoding='UTF-8') as fp:
        fp.write(response.text)