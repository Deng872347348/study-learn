# import requests
#
# # 请求的网站地址
# url = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
#
# # 携带表单参数，发送post
# headers ={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
#     'referer': 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php',
#
# }
# postdata = {
#     'log': 'kaikeba',
#     'pwd': 'kaikeba888'
# }
#
# response =requests.post(url=url,headers=headers,data=postdata)
# print(response.content.decode('utf-8'))
#
# # cookie参数
