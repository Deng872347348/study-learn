from matplotlib import  pyplot as  plt

fig=plt.figure(figsize=(20,8),dpi=80)


x=range(2,26,2)
y=[15,13,14.5,17,20,25,26,26,24,22,18,15]

plt.plot(x,y)
plt.savefig("./sig_size.jpg")  #->保存图片
            #可以保存为svg这种矢量图格式,放大不会有锯

plt.show()