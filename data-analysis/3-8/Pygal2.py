import pygal
x_data=['2011','2012','2013','2014','2015','2016','2017']
#定义2个列表分别作为两组柱状图的轴数据
y_data=[58000.60200,63000,71000,84000,90500,107000]
y_data2=[52000,54200,51500,58300,56800,59500,62700]
#创建pypgal.Bar对象，柱状图
bar=pygal.Bar()
#添加两组代表条形的数据
bar.add('C语言基础',y_data)
bar.add('Python语言基础',y_data2)
#设置x轴的刻度值
bar.x_labels=x_data
bar.title='编程教程的历年销量'
#设置x,y轴的标题
bar.x_title='年份'
bar.x_title='销量'
#指定将数据图输出到SVG文件中
#设置数据图四周的页边距
#也可以通过margin_bottom,margin_left,margin_right,margin_top 只设置单独一边的页边距
bar.margin=35
#隐藏x轴上的网格线
bar.show_y_guides=False
#显示x轴上的网格线‘
bar.show_y_guides=True
#指定将数据图输出到SVG文件中
bar.render_to_file('fk_books_2.svg')