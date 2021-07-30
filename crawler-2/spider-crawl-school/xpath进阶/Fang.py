import os
import re
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}

path = 'Fang/'
if not os.path.exists(path):
    os.makedirs(path)


def crawl(url):
    response = requests.get(url, headers).content.decode('gbk')
    sel = etree.HTML(response)

    # try:
    li_list = sel.xpath('//*[@id="newhouse_loupai_list"]/ul/li')
    'https://cs.newhouse.fang.com/loupan/2710190146.htm'
    for li in li_list:
        url_detail = li.xpath('.//*[@class="nlcd_name"]/a/@href')
        if url_detail:
            url_detail = 'https:' + url_detail[0]

            detail_response = requests.get(url=url_detail, headers=headers).content.decode('gbk')
            sel = etree.HTML(detail_response)

            # 楼盘名
            name = sel.xpath('//h1/strong/text()')[0]

            # 价格
            price = sel.xpath('//span[@class="prib cn_ff"]/text() | //div[@class="inf_left fl mr30"]/text()[last()]')
            price = ''.join(price).strip()

            # 评分
            score = sel.xpath('//div[@class="tit"]/a/text()')[0].strip()

            # 咨询电话
            phone = sel.xpath('//p[@class="phone_num"]/span[2]/text()')[0]

            # 更多详情数据url地址
            url_detail2 = 'https:' + sel.xpath('//div[@class="fl more"]/p/a/@href')[0]
            detail_response2 = requests.get(url=url_detail2, headers=headers).content.decode('gbk')
            sel2 = etree.HTML(detail_response2)

            # 物业类别
            category = sel2.xpath('//div[@class="main-item"][1]/ul/li[1]/div[2]/text()')[0].strip()

            # 装修状况
            decoration_status = sel2.xpath('//div[@class="main-item"][1]/ul/li[2]/div[2]/li[2]/div[2]/text()')[0].strip()

            # 环线位置
            loop_location = sel2.xpath('//div[@class="main-item"][1]/ul/li[2]/div[2]/li[4]/div[2]/text()')
            loop_location = ''.join(loop_location).strip()

            # 楼盘地址
            # //div[@class="main-item"][1]/ul/li[8]/div[2]/text()
            address = sel2.xpath('//div[@class="main-item"][1]/ul/li[2]/div[2]/li[6]/div[2]/text()')
            address = ''.join(address).strip()

            # 小区占地面积
            total_area = sel2.xpath('//div[@class="main-item"][3]/ul/li[1]/div[2]/text()')[0]

            # 绿化率
            greening_rate = sel2.xpath('//div[@class="main-item"][3]/ul/li[4]/div[2]/text()')[0]

            # 停车位
            parking_lot = sel2.xpath('//div[@class="main-item"][3]/ul/li[5]/div[2]/text()')[0]

            # 物业费
            property_fee = sel2.xpath('//div[@class="main-item"][3]/ul/li[9]/div[2]/text()')[0].strip()

            # 物业公司
            property_company = sel2.xpath('//div[@class="main-item"][3]/ul/li[8]/div[2]/a/text()')
            property_company = ''.join(property_company)

            # 简介
            # '//div[@class="main-item"][6]/p/text()' 在浏览器中可以定位到，但在此无数据
            introduction = sel2.xpath('//p[@class="intro"]/text()')
            introduction = ''.join(introduction).strip()

            with open(path+name+'.txt', 'w', encoding='utf-8') as f:
                f.writelines([name+'\n', price+'\n', score+'\n', phone+'\n', category+'\n', decoration_status+'\n',
                              loop_location+'\n', address+'\n', total_area+'\n', address+'\n', greening_rate+'\n',
                              parking_lot+'\n', property_fee+'\n', property_company+'\n', introduction])
            print(name+"房屋数据写入完毕")
    # except Exception as e:
    #     print(e)


if __name__ == '__main__':
    url_list = ['https://cs.newhouse.fang.com/house/s/b9{}/'.format(i) for i in range(4, 10)]
    for url in url_list:
        crawl(url)
