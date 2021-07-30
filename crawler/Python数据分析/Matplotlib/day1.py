import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# plt.show()

# fig = plt.figure()  # an empty figure with no Axes
# fig, ax = plt.subplots()  # a figure with a single Axes
# fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# plt.show()


# from pylab import *
#
# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)

#
# import  numpy as np
# import  matplotlib.pyplot as plt
# X=np.linspace(-np.pi,np.pi,256,endpoint=True)
# C,S=np.cos(X),np.sin(X)
#
# plt.plot(X,C)
# plt.plot(X,S)
# plt.show()

#导入 matplotlib 的所有内容(numpy 可以用np这个名字来使用

from  pylab import *
#创建一个8*6点(point)的图，并设置分辨率为80
figure(figsize=(8,6),dpi=80),
#创建一个新的1*1的子图，接下来的图样绘制在其中的第一块(也是唯一的一块)
subplot(1,1,1)

X=np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S=np.cos(X),np.sin(X)
#绘制余弦曲线，使用蓝色的，连续的，宽度为1(像素)的线条
plot(X,C,color='blue',linewidth=1.0,linestyle="-")
#绘制正弦曲线，使用绿色的，连续，宽度为1(像素)的线条

plot(X,S,color="green",linewidth=1.0,linestyle="-")

#设置横幅的上下限
xlim(-4.0,4.0)

# 设置横轴记号
xticks(np.linspace(-4,4,9,endpoint=True))

# 设置纵轴的上下限
ylim(-1.0,1.0)

# 设置纵轴记号
yticks(np.linspace(-1,1,5,endpoint=True))

# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
show()
