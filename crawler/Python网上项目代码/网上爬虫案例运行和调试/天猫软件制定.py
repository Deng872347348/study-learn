# -*- coding：utf-8 -*-
# @程序作者：那年那棵树
# @功能描述：天猫软件制定
# @Time : 2021/3/10 20:29
from requests_html import HTMLSession
import tkinter as tk
import xlsxwriter as xw
import xlrd
import re
import time
from datetime import date


window = tk.Tk()
window.title('药物！！！')
window.geometry('500x300+500+200')

workbook1 = xlrd.open_workbook('D://测试/店铺热销品.xlsx')
worksheet1 = workbook1.sheet_by_name('医疗器械&中药饮片')
worksheet2 = workbook1.sheet_by_name('保健食品')
# worksheet3 = workbook1.sheet_by_name('处方药Rx')
worksheet4 = workbook1.sheet_by_name('非处方药OTC')
workbook2 = xw.Workbook('D://测试/动态抓取qqq.xlsx')
worksheet21 = workbook2.add_worksheet('医疗器械&中药饮片')
worksheet22 = workbook2.add_worksheet('保健食品')
worksheet24 = workbook2.add_worksheet('非处方药OTC')
rows = worksheet1.nrows
n = tuple(worksheet1.row_values(0))
worksheet21.write_row('A1', n)
for i in range(1, rows):
    worksheet21.write(f'A{i+1}', worksheet1.row_values(i)[0])
    worksheet21.write(f'B{i+1}', worksheet1.row_values(i)[1])
    worksheet21.write(f'C{i+1}', worksheet1.row_values(i)[2])
    worksheet21.write(f'D{i+1}', worksheet1.row_values(i)[3])
    worksheet21.write(f'E{i + 1}', str(date.today()))
list1 = []
for i in range(1, worksheet1.nrows):
    list1.append(worksheet1.row_values(i)[2])
rows = worksheet2.nrows
n = tuple(worksheet2.row_values(0))
worksheet22.write_row('A1', n)
for i in range(1, rows):
    worksheet22.write(f'A{i+1}', worksheet2.row_values(i)[0])
    worksheet22.write(f'B{i+1}', worksheet2.row_values(i)[1])
    worksheet22.write(f'C{i+1}', worksheet2.row_values(i)[2])
    worksheet22.write(f'D{i+1}', worksheet2.row_values(i)[3])
    worksheet22.write(f'E{i + 1}', str(date.today()))
list2 = []
for i in range(1, worksheet2.nrows):
    list2.append(worksheet2.row_values(i)[2])
rows = worksheet4.nrows
n = tuple(worksheet4.row_values(0))
worksheet24.write_row('A1', n)
for i in range(1, rows):
    worksheet24.write(f'A{i+1}', worksheet4.row_values(i)[0])
    worksheet24.write(f'B{i+1}', worksheet4.row_values(i)[1])
    worksheet24.write(f'C{i+1}', worksheet4.row_values(i)[2])
    worksheet24.write(f'D{i+1}', worksheet4.row_values(i)[3])
    worksheet24.write(f'E{i + 1}', str(date.today()))
list4 = []
for i in range(1, worksheet4.nrows):
    list4.append(worksheet4.row_values(i)[2])

def p1():
    url = 'http://list.tmall.com/search_product.htm?'
    session = HTMLSession()

    # def get_totalPage(params, url):
    #     r = session.get(url=url, params=params)
    #     totalPage = int(r.html.find('[name="totalPage"]', first=True).attrs.get('value'))  # 获取总页数
    #     params['totalPage'] = totalPage  # 更新总页数
    #
    # def get_params(params, totalPage):
    #     for i in range(1, totalPage + 1):
    #         params['jumpto'] = i
    #         yield params

    def get_product_info(params, url, count):
        r = session.get(url=url, params=params)
        product_element_list = r.html.find('.product')
        list_product_sell = []
        list_product_shopper = []
        list_product_price = []
        for product_element in product_element_list:
            product_price = product_element.find('em', first=True).attrs.get('title')
            product_shopper = product_element.find('[class=productShop] a', first=True).text
            product_sell = product_element.find('[class=productStatus] em', first=True).text
            list_product_sell.append(eval(re.findall('\d+', product_sell)[0]))
            list_product_shopper.append(product_shopper)
            list_product_price.append(eval(product_price))
        pri = []
        for o in list_product_price:
            pri.append(o)
        pri.sort()
        sell = []
        for o in list_product_sell:
            sell.append(o)
        sell.sort(reverse=True)
        if len(sell) == 0:
            worksheet21.write(f'F{count + 2}', '下架')
        # for name in list_product_shopper:
        if '百信大药房旗舰店' in list_product_shopper:
            print(count)
            dex = list_product_shopper.index('百信大药房旗舰店')
            worksheet21.write(f'S{count + 2}', pri.index(list_product_price[dex]) + 1)
            worksheet21.write(f'O{count + 2}', dex + 1)
            worksheet21.write(f'P{count + 2}', sell.index(list_product_sell[dex]) + 1)
            worksheet21.write(f'F{count + 2}', list_product_price[dex])
            worksheet21.write(f'N{count + 2}', list_product_sell[dex])
            worksheet21.write(f'Q{count + 2}', max(list_product_sell))
            worksheet21.write(f'V{count + 2}', len(list_product_sell))
            worksheet21.write(f'T{count + 2}', min(list_product_price))
            worksheet21.write(f'U{count + 2}', list_product_shopper[list_product_price.index(min(list_product_price))])
            index1 = list_product_sell.index(max(list_product_sell))  # 位置
            worksheet21.write(f'H{count + 2}', list_product_shopper[index1])
            worksheet21.write(f'I{count + 2}', list_product_price[index1])
            list_product_sell.pop(index1)
            list_product_price.pop(index1)
            list_product_shopper.pop(index1)
            index2 = list_product_sell.index(max(list_product_sell))
            worksheet21.write(f'J{count + 2}', list_product_shopper[index2])
            worksheet21.write(f'K{count + 2}', list_product_price[index2])
            list_product_sell.pop(index2)
            list_product_price.pop(index2)
            list_product_shopper.pop(index2)
            index3 = list_product_sell.index(max(list_product_sell))
            worksheet21.write(f'L{count + 2}', list_product_shopper[index3])
            worksheet21.write(f'M{count + 2}', list_product_price[index3])
            for product_element in product_element_list:
                product_price = product_element.find('em', first=True).attrs.get('title')
                product_title = product_element.find('[class=productTitle] a', first=True).attrs.get('title')
                product_shopper = product_element.find('[class=productShop] a', first=True).text
                product_sell = product_element.find('[class=productStatus] em', first=True).text
                print(product_price)  # 商品价格
                print(product_title)  # 商品标题
                print(product_shopper)  # 商家
                print(product_sell)  # 卖出数
        else:
            worksheet21.write(f'Q{count + 2}', max(list_product_sell))
            worksheet21.write(f'V{count + 2}', len(list_product_sell))
            worksheet21.write(f'T{count + 2}', min(list_product_price))
            worksheet21.write(f'U{count + 2}', list_product_shopper[list_product_price.index(min(list_product_price))])
            index1 = list_product_sell.index(max(list_product_sell))  # 位置
            worksheet21.write(f'H{count + 2}', list_product_shopper[index1])
            worksheet21.write(f'I{count + 2}', list_product_price[index1])
            list_product_sell.pop(index1)
            list_product_price.pop(index1)
            list_product_shopper.pop(index1)
            index2 = list_product_sell.index(max(list_product_sell))
            worksheet21.write(f'J{count + 2}', list_product_shopper[index2])
            worksheet21.write(f'K{count + 2}', list_product_price[index2])
            list_product_sell.pop(index2)
            list_product_price.pop(index2)
            list_product_shopper.pop(index2)
            index3 = list_product_sell.index(max(list_product_sell))
            worksheet21.write(f'L{count + 2}', list_product_shopper[index3])
            worksheet21.write(f'M{count + 2}', list_product_price[index3])
            for product_element in product_element_list:
                product_price = product_element.find('em', first=True).attrs.get('title')
                product_title = product_element.find('[class=productTitle] a', first=True).attrs.get('title')
                product_shopper = product_element.find('[class=productShop] a', first=True).text
                product_sell = product_element.find('[class=productStatus] em', first=True).text
                print(product_price)  # 商品价格
                print(product_title)  # 商品标题
                print(product_shopper)  # 商家
                print(product_sell)  # 卖出数


    count = -1
    for n in list1:
        params = {
            'totalPage': 1,
            'jumpto': 1,
            'q': n

        }
        count += 1
        try:
            get_product_info(params, url, count)
        except:
            pass


b1 = tk.Button(window, text='医疗器械&中药饮片', width=20, height=2, bg='skyblue', command=p1)
b1.pack()
def p2():
    url = 'http://list.tmall.com/search_product.htm?'
    session = HTMLSession()
    def get_product_info(params, url, count):
        r = session.get(url=url, params=params)
        product_element_list = r.html.find('.product')
        list_product_sell = []
        list_product_shopper = []
        list_product_price = []
        for product_element in product_element_list:
            product_price = product_element.find('em', first=True).attrs.get('title')
            product_shopper = product_element.find('[class=productShop] a', first=True).text
            product_sell = product_element.find('[class=productStatus] em', first=True).text
            list_product_sell.append(eval(re.findall('\d+', product_sell)[0]))
            list_product_shopper.append(product_shopper)
            list_product_price.append(eval(product_price))
        pri = []
        for o in list_product_price:
            pri.append(o)
        pri.sort()
        sell = []
        for o in list_product_sell:
            sell.append(o)
        sell.sort(reverse=True)
        if len(sell) == 0:
            worksheet22.write(f'F{count + 2}', '下架')
        if '百信大药房旗舰店' in list_product_shopper:
            print(count)
            dex = list_product_shopper.index('百信大药房旗舰店')
            worksheet22.write(f'S{count + 2}', pri.index(list_product_price[dex]) + 1)
            worksheet22.write(f'O{count + 2}', dex + 1)
            worksheet22.write(f'P{count + 2}', sell.index(list_product_sell[dex]) + 1)
            worksheet22.write(f'F{count + 2}', list_product_price[dex])
            worksheet22.write(f'N{count + 2}', list_product_sell[dex])
            worksheet22.write(f'Q{count + 2}', max(list_product_sell))
            worksheet22.write(f'V{count + 2}', len(list_product_sell))
            worksheet22.write(f'T{count + 2}', min(list_product_price))
            worksheet22.write(f'U{count + 2}', list_product_shopper[list_product_price.index(min(list_product_price))])
            index1 = list_product_sell.index(max(list_product_sell))  # 位置
            worksheet22.write(f'H{count + 2}', list_product_shopper[index1])
            worksheet22.write(f'I{count + 2}', list_product_price[index1])
            list_product_sell.pop(index1)
            list_product_price.pop(index1)
            list_product_shopper.pop(index1)
            index2 = list_product_sell.index(max(list_product_sell))
            worksheet22.write(f'J{count + 2}', list_product_shopper[index2])
            worksheet22.write(f'K{count + 2}', list_product_price[index2])
            list_product_sell.pop(index2)
            list_product_price.pop(index2)
            list_product_shopper.pop(index2)
            index3 = list_product_sell.index(max(list_product_sell))
            worksheet22.write(f'L{count + 2}', list_product_shopper[index3])
            worksheet22.write(f'M{count + 2}', list_product_price[index3])
            for product_element in product_element_list:
                product_price = product_element.find('em', first=True).attrs.get('title')
                product_title = product_element.find('[class=productTitle] a', first=True).attrs.get('title')
                product_shopper = product_element.find('[class=productShop] a', first=True).text
                product_sell = product_element.find('[class=productStatus] em', first=True).text
                print(product_price)  # 商品价格
                print(product_title)  # 商品标题
                print(product_shopper)  # 商家
                print(product_sell)  # 卖出数
        else:
            worksheet22.write(f'Q{count + 2}', max(list_product_sell))
            worksheet22.write(f'V{count + 2}', len(list_product_sell))
            worksheet22.write(f'T{count + 2}', min(list_product_price))
            worksheet22.write(f'U{count + 2}', list_product_shopper[list_product_price.index(min(list_product_price))])
            index1 = list_product_sell.index(max(list_product_sell))  # 位置
            worksheet22.write(f'H{count + 2}', list_product_shopper[index1])
            worksheet22.write(f'I{count + 2}', list_product_price[index1])
            list_product_sell.pop(index1)
            list_product_price.pop(index1)
            list_product_shopper.pop(index1)
            index2 = list_product_sell.index(max(list_product_sell))
            worksheet22.write(f'J{count + 2}', list_product_shopper[index2])
            worksheet22.write(f'K{count + 2}', list_product_price[index2])
            list_product_sell.pop(index2)
            list_product_price.pop(index2)
            list_product_shopper.pop(index2)
            index3 = list_product_sell.index(max(list_product_sell))
            worksheet22.write(f'L{count + 2}', list_product_shopper[index3])
            worksheet22.write(f'M{count + 2}', list_product_price[index3])
            for product_element in product_element_list:
                product_price = product_element.find('em', first=True).attrs.get('title')
                product_title = product_element.find('[class=productTitle] a', first=True).attrs.get('title')
                product_shopper = product_element.find('[class=productShop] a', first=True).text
                product_sell = product_element.find('[class=productStatus] em', first=True).text
                print(product_price)  # 商品价格
                print(product_title)  # 商品标题
                print(product_shopper)  # 商家
                print(product_sell)  # 卖出数
    count = -1
    for n in list2:
        params = {
            'totalPage': 1,
            'jumpto': 1,
            'q': n

        }
        count += 1
        try:
            get_product_info(params, url, count)
        except:
            print('error')
            pass
b2 = tk.Button(window, text='保健食品', width=20, height=2, bg='skyblue', command=p2)
b2.pack()
def p4():
    url = 'http://list.tmall.com/search_product.htm?'
    session = HTMLSession()
    def get_product_info(params, url, count):
        r = session.get(url=url, params=params)
        product_element_list = r.html.find('.product')
        list_product_sell = []
        list_product_shopper = []
        list_product_price = []
        for product_element in product_element_list:
            product_price = product_element.find('em', first=True).attrs.get('title')
            product_shopper = product_element.find('[class=productShop] a', first=True).text
            product_sell = product_element.find('[class=productStatus] em', first=True).text
            list_product_sell.append(eval(re.findall('\d+', product_sell)[0]))
            list_product_shopper.append(product_shopper)
            list_product_price.append(eval(product_price))
        pri = []
        for o in list_product_price:
            pri.append(o)
        pri.sort()
        sell = []
        for o in list_product_sell:
            sell.append(o)
        sell.sort(reverse=True)
        if len(sell) == 0:
            worksheet24.write(f'F{count + 2}', '下架')
        if '百信大药房旗舰店' in list_product_shopper:
            print(count)
            dex = list_product_shopper.index('百信大药房旗舰店')
            worksheet24.write(f'S{count + 2}', pri.index(list_product_price[dex]) + 1)
            worksheet24.write(f'O{count + 2}', dex + 1)
            worksheet24.write(f'P{count + 2}', sell.index(list_product_sell[dex]) + 1)
            worksheet24.write(f'F{count + 2}', list_product_price[dex])
            worksheet24.write(f'N{count + 2}', list_product_sell[dex])
            worksheet24.write(f'Q{count + 2}', max(list_product_sell))
            worksheet24.write(f'V{count + 2}', len(list_product_sell))
            worksheet24.write(f'T{count + 2}', min(list_product_price))
            worksheet24.write(f'U{count + 2}', list_product_shopper[list_product_price.index(min(list_product_price))])
            index1 = list_product_sell.index(max(list_product_sell))  # 位置
            worksheet24.write(f'H{count + 2}', list_product_shopper[index1])
            worksheet24.write(f'I{count + 2}', list_product_price[index1])
            list_product_sell.pop(index1)
            list_product_price.pop(index1)
            list_product_shopper.pop(index1)
            index2 = list_product_sell.index(max(list_product_sell))
            worksheet24.write(f'J{count + 2}', list_product_shopper[index2])
            worksheet24.write(f'K{count + 2}', list_product_price[index2])
            list_product_sell.pop(index2)
            list_product_price.pop(index2)
            list_product_shopper.pop(index2)
            index3 = list_product_sell.index(max(list_product_sell))
            worksheet24.write(f'L{count + 2}', list_product_shopper[index3])
            worksheet24.write(f'M{count + 2}', list_product_price[index3])
            for product_element in product_element_list:
                product_price = product_element.find('em', first=True).attrs.get('title')
                product_title = product_element.find('[class=productTitle] a', first=True).attrs.get('title')
                product_shopper = product_element.find('[class=productShop] a', first=True).text
                product_sell = product_element.find('[class=productStatus] em', first=True).text
                print(product_price)  # 商品价格
                print(product_title)  # 商品标题
                print(product_shopper)  # 商家
                print(product_sell)  # 卖出数
        else:
            worksheet24.write(f'Q{count + 2}', max(list_product_sell))
            worksheet24.write(f'V{count + 2}', len(list_product_sell))
            worksheet24.write(f'T{count + 2}', min(list_product_price))
            worksheet24.write(f'U{count + 2}', list_product_shopper[list_product_price.index(min(list_product_price))])
            index1 = list_product_sell.index(max(list_product_sell))  # 位置
            worksheet24.write(f'H{count + 2}', list_product_shopper[index1])
            worksheet24.write(f'I{count + 2}', list_product_price[index1])
            list_product_sell.pop(index1)
            list_product_price.pop(index1)
            list_product_shopper.pop(index1)
            index2 = list_product_sell.index(max(list_product_sell))
            worksheet24.write(f'J{count + 2}', list_product_shopper[index2])
            worksheet24.write(f'K{count + 2}', list_product_price[index2])
            list_product_sell.pop(index2)
            list_product_price.pop(index2)
            list_product_shopper.pop(index2)
            index3 = list_product_sell.index(max(list_product_sell))
            worksheet24.write(f'L{count + 2}', list_product_shopper[index3])
            worksheet24.write(f'M{count + 2}', list_product_price[index3])
            for product_element in product_element_list:
                product_price = product_element.find('em', first=True).attrs.get('title')
                product_title = product_element.find('[class=productTitle] a', first=True).attrs.get('title')
                product_shopper = product_element.find('[class=productShop] a', first=True).text
                product_sell = product_element.find('[class=productStatus] em', first=True).text
                print(product_price)  # 商品价格
                print(product_title)  # 商品标题
                print(product_shopper)  # 商家
                print(product_sell)  # 卖出数
    count = -1
    for n in list4:
        params = {
            'totalPage': 1,
            'jumpto': 1,
            'q': n

        }
        count += 1
        try:
            get_product_info(params, url, count)
        except:
            pass
b4 = tk.Button(window, text='非处方药OTC', width=20, height=2, bg='skyblue', command=p4)
b4.pack()

window.mainloop()
workbook2.close()
