import requests
from bs4 import BeautifulSoup
from  PIL import Image  #安装pillow
import pytesseract  #python操作tesseract接口库 要安装
from io import BytesIO
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3863.400 QQBrowser/10.8.4334.400',
}
# tesseract_cmd = "D:\tool\tesseract\data\Tesseract-OCR\tesseract.exe"
session = requests.session()
# 登录页
login_login = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
login_response = session.get(url=login_login, headers=header)
login_html = login_response.text

login_soup = BeautifulSoup(login_html, 'lxml')
image_url = 'https://so.gushiwen.cn/' + login_soup.find('img', id='imgCode')['src']

__VIEWSTATE = login_soup.find('input', id='__VIEWSTATE')['value']
__VIEWSTATEGENERATOR = login_soup.find('input', id='__VIEWSTATEGENERATOR')['value']

image_data = session.get(image_url, headers=header)
image = image_data.content
filename = 'imageverify.jpg'
with open(filename, 'wb') as file:
    file.write(image)
# 灰度图处理
img = Image.open(BytesIO(image))
img.show()
threshold = 200
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
img = img.point(table, '1')
security_code = pytesseract.image_to_string(img)
print(security_code)
img.close()
name = '15608471682'  # input('请输入用户名:')
pw = '15608471682.a'  # input('请输入密码:')
code = input('请输入验证码:')

url = 'https://so.gushiwen.cn/user/login.aspx?from='
data = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': name,
    'pwd': pw,
    'code': code,
    'denglu': '登录'
}

response = session.post(url=url, data=data, headers=header)
print("状态码:" + str(response.status_code))
print("历史记录:" + str(response.history))

verify_url = 'http://so.gushiwen.cn/user/collect.aspx'
verify_response = session.get(url=verify_url, data=data)
html = verify_response.text

verify_soup = BeautifulSoup(html, 'lxml')
cont = verify_soup.select('div.shisoncont > div.line > span')
print(cont[1].text)