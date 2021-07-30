
import requests
from  bas4 import BeautifulSoup

resp=requests.get("https://www.umei.cc/")#从服务器拿到源代码
#resp.encode('utf-8')
result=resp.text
print(result)

# #解析html
# main_page=BeautifulSoup(resp.text,'html.parser')
# #从页面中找到某些东西
# #find()赵一个
# #find_all()找所有
# alst=main_page.findall("div",altrs={"class":"TypeList"}).findall("a",altrs={"class":"TypeBigPics"})
#
# for a in alst:
#    print(a.get("href"))
#    #发送请求到子页面，进入到所有小姐姐的页面
#    href=a.get("href")
#    resp1=requests.get(href)
#    resp1.encoding('utf-8')
# 	child_page=beautifulSoup(resp1.text)
# 	child_page.findall