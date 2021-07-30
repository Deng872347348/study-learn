#
# import  re
# html_str = """
#     Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
#     测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
#     Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
#     测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
#     Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月02-18剩余255人
#     python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员
# """
# 使用正则表达式提取工资，比如2,2.5,1.3...
#
# 第二题：提取百度页面中所有a链接的文字
# 比如<a href=http://news.baidu.com name=tj_trnews class=mnav>新闻</a>，使用正则表达式提取文字“新闻”。


#
# resp=r"[^工程师]"  #正则表达式
# salarys=re.findall(resp,html_str,re.S)
# print(salarys)
# for salarys in salarys:
#     print(salarys)

# res=r"[\d.]+万/每?月" #正则表达式
# salarys=re.findall(res,html_str,re.S)
# for salarys in salarys:
#     print(salarys)


# import  requests
# import json
# import re
# def get_url():
#     path="糗事百科"
#     url="https://www.qiushibaike.com/imgrank/"
#     headers={
#         'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.82Safari / 537.36'
#     }
#     response=requests.get(url,headers=headers).text
#     res='<div class="thumb".*?<img src="(.*?) alt.*?</div>'
#     picture=re.findall(res,response,re.S)
#     # print(picture)
#     for i in picture:
#         img_url="https:"+i
#         response=requests.get(url=img_url,headers=headers).content
#         with open("image",'wb') as f:
#             f.write(response)
#
#
#
# if __name__ == '__main__':
#     get_url()
#


import re
html='<div class="content"><span>妈妈带狗子出门，忘记带雨衣了——FB:J L</span></div>'
res='<div class="content".*?<span>(.*?)</span>.*?</div>'
resp=re.findall(res,html,re.S)
print(resp)

