# -*- coding: UTF-8 -*-
"""
@File    ：词云图.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""
import pandas as pd
import jieba
import collections
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取段子数据
datas = pd.read_excel('datas.xlsx')['段子内容']

# 读取停用词数据
with open('stop_words.txt', encoding='utf-8') as f:
    con = f.read().split('\n')    # 得到每一行的停用词
    stop_words = set()
    for i in con:
        stop_words.add(i)

result_list = []
for data in datas:
    # 文本预处理  去除一些无用的字符   只提取出中文出来
    new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
    new_data = "/".join(new_data)
    # 文本分词
    seg_list_exact = jieba.cut(new_data, cut_all=True)
    # 去除停用词和单个词
    for word in seg_list_exact:
        if word not in stop_words and len(word) > 1:
            result_list.append(word)

print(result_list)
# 筛选后统计
word_counts = collections.Counter(result_list)

# 绘制词云
my_cloud = WordCloud(
    background_color='white',  # 设置背景颜色  默认是black
    width=800, height=550,
    font_path='simhei.ttf',   # 设置字体  显示中文
    max_font_size=160,        # 设置字体最大值
    min_font_size=16,         # 设置字体最小值
    random_state=88           # 设置随机生成状态，即多少种配色方案
).generate_from_frequencies(word_counts)

# 显示生成的词云图片
plt.imshow(my_cloud, interpolation='bilinear')
# 显示设置词云图中无坐标轴
plt.axis('off')
plt.show()
