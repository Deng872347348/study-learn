import  requests
from  bs4 import  BeautifulSoup
import  os


alL_url='https://changsha.8684.cn/'
headers={
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
start_html=requests.get(url=alL_url,headers=headers)
print(start_html.text)
soup=BeautifulSoup(start_html.text,'lxml')



