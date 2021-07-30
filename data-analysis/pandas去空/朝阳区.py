import pandas as pd
df=pd.read_excel('朝阳区药品销售数据.xlsx')
#数据清洗
#判断和处理空值
print(pd.isnull(df).sum())

#删除法
print("原数据")
df.dropna(inplace=True)
print("去空格数据形状",df.shape)

#替换法
mean=df['实收金额'].sum()/df['实收金额'].count()
print(mean)
dict={"购药时间":0,"社保卡号":0,"商品编号":0,"商品名称":0,"销售数量":0,"应收金额":0,"实收金额":0}
df.fillna(value=0,inplace=True)
#设置填充值
df.fillna(value=dict,inplace=True)
print('======向前填充=======')
df.fillna(inplace=True,method='ffill')
print(pd.isnull(df).sum())
#处理重复值
# dt=df.duplicated(inplace=True)
print("去重数据形状",df.shape)
df.drop_duplicates(inplace=True,subset=['购药时间','社保卡号'])
print("去重数据形状",df.shape)

#处理异常值
df['社保卡号']=df['社保卡号'].astype('str')
print(df.info)
print('======查看是否有异常数据======')
print(df.describe())

condition=df['销售数量']>0
df=df.loc[condition,:]
print(df.describe)
