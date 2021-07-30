#第一步确定url
import  requests
from lxml import etree

def stripText(textList):

    str_list=""
    for item in textList:
        item_str=item.replace('\n',"").replace('\r',"").replace('\t',"").replace('/',"").replace('-',"")
        #item_str = item.strip() #当参数为空时，默认删除字符串两端的空白字符（包括'\n','\r','\t','')
        if item_str!='':
            if str_list!='':
                str_list=str_list+","+item_str
            else:
                str_list=item_str
        return  str_list
#U-A伪装
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
#第一步，确定请求的URL
#url=

base_url="https://cs.newhouse.fang.com/house/s/b9"

end_page=input("请输入要结束页：")
for p in range(1,int(end_page)+1):
    page=str(p)
    url=base_url+page+"/"
    param={
        'ctm': '1.cs.xf_search.page.' + page
    }

    #第二步，发出HTTP请求
    response=requests.get(url=base_url,headers=headers)
    response=response.content.decode('gbk')
    #第三步:获取响应数据
    html_content=response
    #第四步进行持久化
    with open("fang"+page+".html",'w',encoding='gbk') as fp:
        fp.write(html_content)

    # parse=etree.HTMLParser(encoding='gbk')
    # tree=etree.parse("fang"+page+".html",parser=parse)
    # print(etree.tostring(tree,encoding='gbk').decode("gbk"))
    tree=etree.HTML(html_content)
    item_xpath="//div[@class='nhouse_list_content']/div[@class='nhouse_list']/div[@id='newhouse_loupai_list']/ul/li/div[@class='clearfix']"
    item_list=tree.xpath(item_xpath)
    print(item_list)
    all_content=[]

    for item in item_list:
             #总地址
        # if item_xpath(".//div[@class='nlc_details']/div[@class='house_value clearfix']/div[@id='sjina_D52_02']/a")==0:
        #     continue
        item_dic={}

        #楼盘名
        name_xpath=".//div[@class='nlc_details']/div[@class='house_value clearfix']/div[@id='sjina_D52_02']/a/text()"
        name_list=item.xpath(name_xpath)
        item_dic["name"]=stripText(name_list)
        print(item_dic["name"])

        #楼盘所在区
        dist_xpath = ".//div[@class='nlc_details']/div[@class='relative_message clearfix']/div/a/span/text()"
        dist_list = item.xpath(dist_xpath)
        item_dic["dist"]=stripText(dist_list)
        print(item_dic["dist"])

        #楼盘地址
        addr_xpath = ".//div[@class='nlc_details']/div[@class='relative_message clearfix']/div[@class='address']/a/text()"
        addr_list = item.xpath(addr_xpath)
        item_dic["addr"] = stripText(addr_list)
        print(item_dic["addr"])

        #楼盘价格
        price_xpath =".//div[@class='nlc_details']/div[@class='nhouse_price']/span/text()"
        price_list = item.xpath(price_xpath)
        item_dic["price"] = stripText(price_list)
        print(item_dic["price"])

        #楼盘标签
        label_xpath = ".//div[@class='nlc_details']/div[@class='fangyuan pr']/a/text()"
        label_list = item.xpath(label_xpath)
        item_dic["label"] = stripText(label_list)
        print(item_dic["label"])

        # 楼盘居室
        room_xpath = ".//div[@class='nlc_details']/div[@class='house_type clearfix']/child::node()/text()"
        room_list = item.xpath(room_xpath)
        item_dic["room"] = stripText(room_list)
        print(item_dic["room"])

        # 楼盘面积
        area_xpath =".//div[@class='nlc_details']/div[@class='house_type clearfix']/text()"
        area_list = item.xpath(area_xpath)
        item_dic["area"] = stripText(area_list)
        print(item_dic["area"])

        all_content.append(item_dic)

            # 第四步进行持久化
    with open("fang" + page + ".txt", 'w', encoding='utf-8') as fp:
         for item in all_content:
               fp.write(str(item)+"\n")