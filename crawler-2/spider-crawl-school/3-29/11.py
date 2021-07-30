import requests
import re


def geturls():
    url='http://www.qstheory.cn/dukan/qs/2014/2019-01/01/c_1123924172.htm'
    headers={
        'User - Agent':'Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv: 86.0) Gecko / 20100101Firefox / 86.0'
    }
    response=requests.get(url,headers).content.decode()
    # res = '<a href="(.*?)" target=.*?</a>'
    res='<a href="(.*?)" target=.*?<strong>.*?</strong>'
    ss = re.findall(res, response, re.S)
    urls=ss[1:]
    # return urls
    print(urls)

if __name__ == "__main__":
    geturls()
    # urls = geturls()
    # for x in urls:
    #     print(x)


# import re
# html='<a href="http://www.qstheory.cn/dukan/qs/2018-12/31/c_1123923896.htm" target="_blank"><strong>辩证唯物主义是中国共产党人的世界观和方法论</strong></a>'
#
# res='<a href="(.*?)" target=.*?<strong>.*?</strong></a>'
# ss=re.findall(res,html,re.S)
# print(ss[0])