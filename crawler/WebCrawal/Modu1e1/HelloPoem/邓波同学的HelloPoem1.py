#引入库文件
import  requests
from  lxml import etree
import  xml
#获取url
url="http://www.zgshige.com/c/2020-05-12/13586017.shtml"
#构造伪请求头
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
}
#发送HTTP请求
response=requests.get(url=url,headers=header)
#获取响应数据
html_content=response.text
# with open("poem.html","w",encoding="utf-8") as fp:
#     fp.write(html_content)
#XPath步骤1，创建解析对象
tree=etree.HTML(html_content)
#print(etree.tostring(tree).decode())
all_content=""

# #XPath步骤2，构建xpath对象
# title_xpath="//div//h3"
# #xpath步骤3，进行xpath解析，获取解析结果
# title_list=tree.xpath(title_xpath)
# #print(title_list[0]）
# title=title_list[0]
# all_content=all_content+title+"/n"
# print(all_content)

# #XPath步骤2，构建xpath对象
# author_xpath=""
# #xpath步骤3，进行xpath解析，获取解析结果
# author_list=tree.xpath(author_xpath)
# #print(author_list[0]）
# author=author_list[0]
# all_content=all_content+author+"/n"
# print(all_content)
# author=",".join(author_list).strip("/n")
# #下面的表达方式效果更好
# #author="".join(author_list).strip("/n")
# all_content=all_content+author+"/n"
# print(all_content)

#XPath步骤2，构建xpath对象
poem_xpath="http://www.zgshige.com/c/2020-05-12/13586017.shtml"
#xpath步骤3，进行xpath解析，获取解析结果
poem_list=tree.xpath(poem_xpath)
#print(poem_list[0]）
poem=",".join(poem_list)
all_content=all_content+poem+"/n"
print(all_content)

# #XPath步骤2，构建xpath对象
# detail_xpath=""
# #xpath步骤3，进行xpath解析，获取解析结果
# detail_list=tree.xpath(detail_xpath)
# print(detail_list)
# #detail=",".join(detail_list)
#
# for detail in detail_list:
#     if(detail!="/n"):
#         detail=detail.strip("/u3000 \n")
#         all_content=all_content+detail+"/n"
#         print(all_content)

        #第四步进行持久化
with open("poem.txt","w",encoding="utf-8") as fp:
    fp.write(all_content)
