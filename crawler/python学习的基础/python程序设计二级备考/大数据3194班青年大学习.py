# coding=utf-8
import pandas as pd
import csv
import codecs
def cig_data(file_path1, file_path2):
    data = pd.read_excel(file_path1, sheet_name=0,header=1)
    data.drop_duplicates(subset='登记姓名', keep='first', inplace=True)
    print(data['登记姓名'])
    data_list = data['登记姓名'].values.tolist()      # 将某一列读到列表中
    print(data_list)
    Df = pd.read_excel(file_path2, sheet_name=0,header=2)
    df_list = Df['姓名'].values.tolist()
    a = [x for x in data_list if x in df_list]  # 两个列表表都存在
    print(a)
    return a
cig_data('D:\QQ\MobileFile\人工智能.xls','D:\QQ\学生花名册（2018级人工智能学院)大数据3182(1).xlsx')
#file_name为写入CSV文件的路径，datas为要写入数据列表
def data_write_csv(file_name, datas):
    file_csv = codecs.open(file_name,'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(data)
    print("保存文件成功，处理结束")
data_write_csv('大数据3182班未学习青年大学习名单.csv',cig_data('D:\QQ\MobileFile\人工智能.xls','D:\QQ\学生花名册（2018级人工智能学院)大数据3182(1).xlsx'))
