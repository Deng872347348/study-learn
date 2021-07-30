import requests
from lxml import etree

def stripText(textList):
    str_list=""
    for item in  textList:
        item_str=item.replace('\r',"").replace('\n',"").replace('\t',"")
        if item_str!='' :
              if item_str!= '':
                  str_list=str_list+item_str
              else:
                  str_list=item_str
        return str_list
url='https://newhouse.fang.com/house/s/'

headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

response=requests.get(url=url,headers=headers)
response.encoding='gbk'
html_code=response.text

with open("fang.html",'w',encoding='gbk') as f:
    f.write(html_code)
    print("你的房天下的数据已经下好了！ ！")

parse=etree.HTMLParser(encoding='gbk')
tree=etree.parse('fang.html',parser=parse)
#print(etree.tostring(tree,encoding='gbk').decode('gbk'))


item_xpath='//div[@class="nhouse_list_content"]/div[@class="nhouse_list"]/div[@id="newhouse_loupai_list"]/ul/li'
item_list=tree.xpath(item_xpath)
print(item_xpath)
for item in item_list:
    if item.xpath('.//div[@class="nlc_details"]/div[@class="house_value clearfix"]/div[@class="nlcd_name"]/a')==0:
        continue
    item_dic=[]
    name_xpath='.//div[@class="nlc_details"]/div[@class="house_value clearfix"]/div[@class="nlcd_name"]/a/text()'
    # name_list=item.xpath(name_xpath)[0].text
    name_list= item.xpath(name_xpath)
    item_dic=stripText(name_list)
    print(item_dic)
    #print(name_list)
