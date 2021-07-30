import pandas as pd
import numpy as np

#读取北京的住房数据
file_path_bj=open('data/北京地区信息.csv')
file_data_bjinfo=pd.read_csv(file_path_bj)
print(file_data_bjinfo)
#读取天津的住房数据
file_path_tj=open('data/天津地区信息.csv')
file_data_tianjing=pd.read_csv(file_path_tj)
print(file_data_bjinfo)

#检测bjin数据是否有重复数据：返回True表示重复数据
print(file_data_bjinfo.duplicated())

#检测bjin数据是否有重复数据：返回True表示重复数据
print(file_data_tianjing.duplicated())


#北京地区删除重复数据
print(file_data_bjinfo.drop_duplicates())

#天津地区删除重复数据
print(file_data_tianjing.drop_duplicates())

#判断天津地区数据是否有空值
print(file_data_tianjing.isnull())

#计算常住人口的平均数，设置为float类型并且保留两位数字

population=float("{:.2f}".format(file_data_tianjing['常住人口（万人）'].mean()))

#以字典映射的形式将需要填充的数据进行对应
values={'常住人口（万人）':population}

file_data_tjinfo=file_data_tianjing.fillna(value=values)
print(file_data_tjinfo)

#异常值的处理
#对北京地区异常值得处理
file_data_bjinfo.boxplot(column=['行政面积（K㎡）','户籍人口（万人）','男性','女性','GDP（亿元）' ,'常住人口（万人）'])
#对天津地区信息进行异常值检测
file_data_tianjing.boxplot(column=['行政面积（K㎡）','户籍人口（万人）','男性','女性','GDP（亿元）' ,'常住人口（万人）'])

#对两个地区的数据进行一个合并
pd.concat([file_data_bjinfo,file_data_tianjing],ignore_index=True)