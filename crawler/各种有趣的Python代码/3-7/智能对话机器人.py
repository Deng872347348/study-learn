import requests
url='http://api.qingyunke.com/api.php?key=free&appid=0&msg='
#input()接收用户想要表达的话
allen=input()#input() 接收用户想要说的话
#input()接收用户想要表达的话
# print(allen)
# print(url)

resp=requests.get(url)
print(resp)

