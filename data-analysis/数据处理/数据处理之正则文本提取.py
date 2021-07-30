'''
提取Mi,Xr,可以看到该提取字符前面没有空格了，所以将正则表达式稍作
修改删除空格，即可得到需要的效果
'''
import pandas as pd
x=['Aaa,Mi.mmmki','Aaa,Xr.mmmki']
x=pd.DataFrame(x)
x[1]=x[0].str.extract('([A-Za-z]+)\.')
