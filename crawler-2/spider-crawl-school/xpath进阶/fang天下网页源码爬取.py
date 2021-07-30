#coding=gbk
from  lxml import etree
import requests


#请求响应数据

url='https://wuhan.esf.fang.com/'
headers={
    "cookie": "global_cookie=vu2iy4m98uigeoordz4pbbzgw18kkf2t8xq; newhouse_user_guid=B5EC4245-FC89-5897-9C74-80BE207B6809; new_search_uid=fa1070c0a9632507bef524a59d7034ca; integratecover=1; city=wuhan; __utmc=147393320; __utma=147393320.1161696293.1611730649.1616911597.1616937023.6; __utmz=147393320.1616937023.6.5.utmcsr=wuhan.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; xfAdvLunbo=; g_sourcepage=xf_lp%5Elb_pc; unique_cookie=U_eujv6m6gm8iawfvil1z28kpsn1akmsrevhw*8; searchConN=1_1616937444_727%5B%3A%7C%40%7C%3A%5Dada2268afb4fc0fd20c0d5101bea3075; __utmb=147393320.14.10.1616937023",
    'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36'
}
response=requests.get(url,headers=headers).content.decode('')
# response.encoding='utf-8'
# resp=response.text
# print(resp)
#数据的存储
with open("fang.html",'w',encoding='gbk') as f:
    f.write(resp)

# parse=etree.HTMLParser(encoding='gbk')
# tree=etree.parse('fang.html',parser=parse)
# print(etree.tostring(tree,encoding='gbk').decode('gbk'))