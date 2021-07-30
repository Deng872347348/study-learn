#第一步确定url
import  requests;
#xpath 步骤1：导包.etree不会有提示
from lxml import  etree

def stripText(textList):

    # //将文本列表转化成字符串，并去掉其中包括的/n /t /r /等字符串
    # :param textList 文本列表
    # :return:字符串

    str_list=""
    for item in textList:
        item_str=item.replace('\n',"").repalce('\r',"").replace('\t',"").repalce('/',"").replace('-',"")
        #item_str = item.strip() #当参数为空时，默认删除字符串两端的空白字符（包括'\n','\r','\t','')
        if item_str!='':
            if str_list!='':
                str_list=str_list+","+item_str
            else:
                str_list=item_str
        return  str_list
#U-A伪装
header={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
#第一步，确定请求的URL
#url=

base_url=""

end_page=input("请输入要结束页：")
for p in range(1,int(end_page)+1):
    page=str(p)
    utl=base_url+page+"/"
    param={

    }

    #第二步，发出HTTP请求
    response=requests.get(url=base_url,headers=header)
    response.encoding="gbk"
    #第三步:获取响应数据
    html_content=response.text
    #第四步进行持久化
    with open("fang"+page+".html",'w',encoding='gbk') as fp:
        fp.write(html_content)

        # parse=etree.HTMLParser(encoding='gbk')
        # tree=etree.parse("fang"+page+".html",parser=parse)
        # print(etree.tostring(tree,encoding='gbk').decode("gbk"))

        item_xpath=""
        item_list=tree.xpath(item_xpath)
        print(item_list)
        all_content=[]

    for item in item_list:
            if item_xpath("")==0:
               continue
               item_dic={}

               name_xpath=""
               name_list=item.xpath(name_xpath)
               item_dic["name"]=stripText(name_list)
               print(item_dic["name"])

               dist_xpath=""
               dist_list=item.xpath(dist_xpath)
               item_dic["dist"]=stripText(dist_list)
               print(item_dic["dist"])

               addr_xpath = ""
               addr_list = item.xpath(addr_xpath)
               item_dic["addr"] = stripText(addr_list)
               print(item_dic["addr"])

               price_xpath = ""
               price_list = item.xpath(price_xpath)
               item_dic["price"] = stripText(price_list)
               print(item_dic["price"])

            label_xpath = ""
            label_list = item.xpath(label_xpath)
            item_dic["label"] = stripText(label_list)
            print(item_dic["label"])

            room_xpath = ""
            room_list = item.xpath(room_xpath)
            item_dic["room"] = stripText(room_list)
            print(item_dic["room"])

            area_xpath = ""
            area_list = item.xpath(area_xpath)
            item_dic["area"] = stripText(area_list)
            print(item_dic["area"])

            all_content.append(item_dic)

            # 第四步进行持久化
            with open("fang" + page + ".txt", 'w', encoding='utf') as fp:
                for item in all_content:
                   fp.write(str(item)+"\n")