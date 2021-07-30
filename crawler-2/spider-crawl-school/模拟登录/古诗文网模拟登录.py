import  requests
from  bs4 import  BeautifulSoup
#验证码的识别
import pytesseract
from PIL import  Image
#BytesIO实现在内容总读写bytes
from io import  BytesIO

#全局变量
#U-A
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
#session对象
session=requests.session()
#登录页获取图片的存储
login_url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
#使用session对象发送请求
login_requests=session.get(login_url,headers=headers)
login_html=login_requests.text
#数据分析
login_soup=BeautifulSoup(login_html,'lxml')
image_url='https://so.gushiwen.org'+login_soup.find('img',id='imgCode')['src']
_VIEWSTATE=login_soup.find('input',id='_VIEWSTATE')
_VIEWSTATEGENERATOR=login_soup.find('input',id='_VIEWSTATEGENERATOR')['value']
print(image_url)
print(_VIEWSTATE)
print(_VIEWSTATEGENERATOR)

#发送请求，获取验证码图片，保存到本地
image_data=session.get(image_url,headers=headers)
image=image_data.content
filename='image_verify.jpg'
with open(filename,'wb') as file:
    file.write(image)
#验证码的识别
#将图像文件转成Image实例
img=Image.open(BytesIO(image))
#转成为灰色图像，1：二值图像，灰色图像
img=img.convert('L')
#将图像中的验证码转换为文本验证码
security_code=pytesseract.image_to_string(img)
print("识别出的验证码为:"+security_code)
img.close();

#模拟古诗文网登录
name=input("请输入用户名: ")
pw=input("请输入密码: ")
code=input("请输入识别后的验证码: ")
url=''
data={

}
#seesion保存对登录后的页面发送请求，验证码登录成功
response=requests.post(url,data=data,headers=headers)
print("状态码: "+str(response.status_code))
print("历史记录: "+str(response.history))

#session保存对登录后的页面发送请求，验证登录成功
verify_url='' #登录后的url
#session发送请求
verify_response=session.get(verify_url,headers=headers)
#解析数据，获取账号显示后六位
verify_soup=BeautifulSoup.find(verify_response,'lxml')
cont=verify_soup.select('div.shisoncont div.line')[3].span.text
print("验证你的账户: "+cont)