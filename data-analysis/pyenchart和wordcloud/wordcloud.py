import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
from os import path
import matplotlib.pyplot as plt
#用来正常显示中文
plt.rcParams["font.sans-serif"]=["SimHei"]
#用来正常显示负号
plt.rcParams["axes.unicode_minus"]=False
import os
import random,jieba
import wordcloud
data = open('E:\python社区版\python项目\学校上课数据分析代码\pyenchart和wordcloud\国家综合立体交通网规划纲要.txt', 'r', encoding='utf-8').read()
wordlist = jieba.lcut(data)
strs = ' '.join(wordlist)
mask=np.array(Image.open('E:\python社区版\python项目\学校上课数据分析代码\pyenchart和wordcloud\2 (1).jpg'))
# 生成词云
wc = wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color="white",stopwords={'的','和','与'})
wc.generate(strs)
wc.to_file("中国地图词云图.png")