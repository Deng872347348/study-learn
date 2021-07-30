import requests
from lxml import etree
import pymysql
#确定请求的url

def main():
    base_url="http://csga.changsha.gov.cn/jjzd/csjj_index/topic_4169_"
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
        }
    end_page=input("请输入结束页:")
    for p in range(1,int(end_page)+1):
        url=base_url+str(p)+".shtml"
        response=requests.get(url=url,headers=header)
        response.encoding="utf-8"
        #print(response.text)
        #生成etree对象
        tree=etree.HTML(response.text)
        item_list=tree.xpath("//div[@class='list_content_box']/div[@id='newsdata']/div[@class='info_list_top']/a[@class='morePointer']/@href")
        # print(item_list)
        all_content=[]
        #循环爬取交通详情页面
        for item in item_list:
            r_detail = requests.get(url=item, headers=header)
            r_detail.encoding = "utf-8"
            #print(r_detail.text)
            detail_tree=etree.HTML(r_detail.text)
            #计算表格行的个数
            count=detail_tree.xpath("count(//table/tbody/tr)")
            print(count)
            for row in range(2,int(count)+1):
                traffic_rule=detail_tree.xpath("//table/tbody/tr["+str(row)+"]/td[last()]//text()")[0]
                #print(traffic_rule)  #处罚标准
                traffic_action= detail_tree.xpath("//table/tbody/tr[" + str(row) + "]/td[last()-1]//text()")[0]
                #print(traffic_action) #违法行为
                traffic_type = detail_tree.xpath("//table/tbody/tr[" + str(row) + "]/td[last()-2]//text()")[0]
                #print(traffic_type)  #车辆类型
                traffic_code = detail_tree.xpath("//table/tbody/tr[" + str(row) + "]/td[last()-3]//text()")[0]
                #print(traffic_code)  #车牌号码
                traffic_place = detail_tree.xpath("//table/tbody/tr[" + str(row) + "]/td[last()-4]//text()")[0].replace("\xa0","")
                #print(traffic_place) #违法地点
                traffic_time = detail_tree.xpath("//table/tbody/tr[" + str(row) + "]/td[last()-5]//text()")[0].replace("\xa0","")
                #print(traffic_time)  #违法时间
                traffic_data={
                    'traffic_time':traffic_time,
                    'traffic_place':traffic_place,
                    'traffic_code':traffic_code,
                    'traffic_type':traffic_type,
                    'traffic_action':traffic_action,
                    'traffic_rule':traffic_rule
                }
                # print(traffic_data)
                all_content.append(traffic_data)
                return  all_content
def insertDicData(table,all_content):
    data=all_content[0]
    cols=",".join('`{}`'.format(k) for k in data.keys())
    print(cols)
    cols_value=",".join('%({})s'.format(k) for k in data.keys())
    print(cols_value)
    sql="insert into"+table+"(%s) values(%s)"
    res_sql=sql%(cols,cols_value)
    print(res_sql)
    cursor.executemany(res_sql,all_content)
    db.commit()
if __name__ == '__main__':
  all_content=main()
  db=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",db="trafficdb")
  cursor=db.cursor()
  insertDicData("traffic",all_content)
