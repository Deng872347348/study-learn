import re
import requests

def get_url():
    url='https://s.weibo.com/top/summary'
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36'
    }
    response=requests.get(url,headers).text
    res='<td class="td-02".*?<a href=.*?>(.*?)</a>'
    information=re.findall(res,response,re.S)
    print(information)

    for a in information:
        print(a)
        with open('weibo.txt','a',encoding='gb2312') as f:
            f.write(a+'\n')
            f.close()



if __name__ == '__main__':
    get_url()