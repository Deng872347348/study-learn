# import requests
# import os
# path='Python爬虫学习案例\1-26日学习案例\图片'
# url='https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=587873873,3496120628&fm=26&gp=0.jpg'
# if os.path.exists(path):
#     os.mkdir(path)
# response=requests.get(url).content#将图片转化成二进制数据
# #进行图片数据的数据持久化
# with open("1.jpg",'wb') as f:
#     f.write(response)
#     print("恭喜你图片下载成功! !")

#导包 二维码工具
# from MyQR import myqr
# myqr.run(words='i love you',
#          picture='1.jpg',
#          colorized=True,
#           save_name='3.png')


# from segno import helpers
# data=helpers.make_mecard(
#     name='邓波',
#     email='872347348@qq.com',
#     phone='15608471682'
# )
# data.save('邓波的名片.png',scale=10)

# from MyQR import myqr
# myqr.run(
#     words='http://www.baidu.com', # words中填写链接或者文本内容
#     version=1,  # 控制二维码大小 1~40，建议不要超过5，否则生成时间太长
#     level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
#     picture='1.jpg',  # 背景图片，格式可以是.jpg, .png, .bmp, .gif
#     colorized=True,  # 可以使产生的图片由黑白(False)变为彩色(True)的
#     contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
#     brightness=1.0,  # 用来调节图片的亮度
#     save_name='2.png'
# )

