#import sys #python内置库
import cv2 #计算机视觉领域
import face_recognition #人脸识别库，如果读取图片的话，会是图像矩阵
import  sys
#就是每个图片的rgb
# 1.人脸数据
# 2.算法
# 3.建立模型
# 4.训练模型
# 5.测试模型
# 6.上线使用
import
# 1读取
face_image = face_recognition.load_image_file("E:\python社区版\python项目\深度学习与机器学习\人脸动态追踪\克拉女神江琴 长发美女 红色裙子4K美女壁纸.jpg")#读取图片
# 2进行人脸特征提取 向量化
#128维的五官数据
face_encoding = face_recognition.face_encodings(face_image)
# 3人脸位置
face_locations = face_recognition.face_locations(face_image)
# 判断
n = len(face_encoding)
#如果超过连个人就退出来
if n>2:
    print('超过两个人')
    sys.exit()
face1 = face_encoding[0]
face2 = face_encoding[1]
# 4比较   阈值 tolerance指定容错率，越小越严格
result = face_recognition.compare_faces([face1],face2,tolerance=0.5)
if result == [True] :
    print(1)
    name = 'Yes'
else :
    print(0)
    name = 'No'
#绘图

for i in range(len(face_encoding)):
    face_encoding = face_encoding[i]
    face_location = face_locations[i]
    top,right,bottom,left = face_location
    #画框             图像                  位置          颜色     粗细
    cv2.rectangle(face_image,(left,top),(right,bottom),(0,255,0),2)
    #写字
    cv2.putText(face_image,name,(left,top),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0,2))
face_image_rgb = cv2.cvtColor(face_image,cv2.COLOR_BGR2RGB)
# 展示图像
cv2.imshow("output",face_image_rgb)
#防止闪退
cv2.waitKey(0)





