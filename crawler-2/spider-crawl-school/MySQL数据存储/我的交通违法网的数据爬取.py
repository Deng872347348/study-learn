import requests
from lxml import etree
from fake_useragent import UserAgent
import random
headers={
   'User-Agent':str(UserAgent().random)
}

base_url='http://csga.changsha.gov.cn/jjzd/csjj_index/topic_4169_'
end_page=input("结束页:")
for p in range(1,int(end_page)+1):
    url=base_url+str(p)+".shtml"
    response = requests.get(url=url, headers=headers)

    #返回网页源代码的编码格式
    response.encoding=response.apparent_encoding
    #网页的文本 相当于网页源代码 html
    html_content=response.text
    #测试网页源代是否获取，编码格式是否错误

    #用xpath解析requests响应获取的网页源代码
    tree=etree.HTML(html_content)
    #写xpath表达式
    #一节页面xpath的解析
    item_list=tree.xpath("//a[@class='morePointer']")
    #测试xpath表达式是否正确
    # print(item_list)
    #二级页面的xpath解析
    traffic_list=[]
    for i in item_list:
        #获取网页的二级页面的跳转链接
        href=i.xpath('./@href')
        #测试网页的跳转链接是否被提取出来
        # print(href)
        #对二级页面的链接发起请求，进入二级页面
        response=requests.get(url=href[0],headers=headers)
        #获取二级页面的网页源代码的编码格式
        response.encoding=response.apparent_encoding
        #获取二级页面网页的源代码
        content=response.text
        #用xpath对网页的二级页面进行解析
        tree_html=etree.HTML(content)
        #获取我们需要的详情页面的xpath
        #用count来计算表格tr有多少行，防止超出tr表格的范围，出现下表越界
        count=tree_html.xpath('count(//table/tbody/tr)')
        # print(count)
        for i in range(2,int(count)+1):
            #违法时间
            traffic_time=tree_html.xpath("//table/tbody/tr["+str(i)+"]/td[last()-5]/span//text()")
            print(traffic_time)
            #违法地点
            traffic_site=tree_html.xpath("//table/tbody/tr["+str(i)+"]/td[last()-4]/span//text()")[0].replace('\xa0','')
            # print(traffic_site)
            #车牌号码
            traffic_number=tree_html.xpath("//table/tbody/tr["+str(i)+"]/td[last()-3]/span//text()")
            traffic_number=''.join(traffic_number).strip()
            # print(traffic_number)
            #车辆类型
            traffic_type=tree_html.xpath("//table/tbody/tr["+str(i)+"]/td[last()-2]/span//text()")[0]
            # print(traffic_type)
            #违法行为
            traffic_behavior=tree_html.xpath("//table/tbody/tr["+str(i)+"]/td[last()-1]/span//text()")[0]
            # print(traffic_behavior)
            #处罚标准
            traffic_rules=tree_html.xpath("//table/tbody/tr["+str(i)+"]/td[last()]/span//text()")[0]
            # print(traffic_rules)
            # 定义一个字典，用来存储用xpath解析得到到的数据
            # item_detail={
            #     'traffic_rules':traffic_rules,
            #     'traffic_behavior':traffic_behavior,
            #     'traffic_type':traffic_type,
            #     'traffic_number':traffic_number,
            #     'traffic_site': traffic_site,
            #     'traffic_time':traffic_time,
            # }
            # print(item_detail)
            # traffic_list.append(item_detail)



# import pymysql
# def insertDicData(table,all_content):
#     data=all_content[0]
#     cols=','.join('{}'.format(k) for  k in data.keys())
#     print(cols)
#     cols_value=','.join('%({})s'.format(k) for  k in data.keys())
#     print(cols_value)
#     sql="insert into"+table+"(%s) values(%s)"
#     res_sql=sql%(cols,cols_value)
#     print(res_sql)
#     cursor.executemany(res_sql,all_content)
#     db.commit()
# de=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="872347348",db="")
# cursor=db.cursor()
# insertDicData("",all_content)





