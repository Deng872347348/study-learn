import requests
from bs4 import BeautifulSoup

with open('1.html','r',encoding='utf-8') as f:
    html=f.read()

soup=BeautifulSoup(html,'lxml')
aa=soup.select('div.left > ul > li>p')
data=[]
for p in soup.find('div', attrs={'class', 'left'}).find_all('p'):
   # print(p.getText())
   data.append(p.getText())
print(data)
# for a in range(len(aa)):
#
# print(ss)
print("我能一打5个人，你们都是菜鸡，哈哈，我就是这么的牛逼，哈哈哈，王者荣耀是和没有以西体育的游戏")
