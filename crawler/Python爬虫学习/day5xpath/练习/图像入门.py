from PIL import  Image#深度 处理图像
import numpy as np #像素处理 科学运算

#读取图片 ->图片转变成 数组
#回是处理 -》降低 图片的计算强度
L=np.asarray(Image.open(r'11.jpg').convert('L')).astype('float')

depth=10. #(0-100) 深度值
grad=np.gradient(L) #获取图像灰度的梯度值
grad_x,grad_y=grad #横向图像梯度
grad_x=grad_x*depth/100
grad_y=grad_y*depth/100

#获取图片对角的平方根
A=np.sqrt(grad_x**2+grad_y**2+1.)
uni_x=grad_x/A
uni_y=grad_y/A
uni_z=1. /A

#处理光源
el=np.pi/2.2 #光源俯视角度，弧度值
az=np.pi/4 #方位角度
dx=np.cos(el)*np.cos(az) #x轴影响
dy=np.cos(el)*np.sin(az) #y轴影响
dz=np.sin(el) #z轴


#光源归一化
gd=255*(dx*uni_x+dy*uni_y+dz*uni_z)
gd=gd.clip(0,255)

#把数组转变成图片 重构图像
im=Image.fromarray(gd.astype('uint8'))
im.save(r'123.jpg')