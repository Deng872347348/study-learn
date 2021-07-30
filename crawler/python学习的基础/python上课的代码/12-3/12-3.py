# FileName = '八不准.txt'
# with open('八不准.txt', 'r', encoding='utf-8') as f1:
#     if f1:
#         # 找到索引下标
#         index = FileName.rfind('.')
#         if index > 0:
#             FageName = FileName[index:]
#         FaName = '八不准' + '副本' + FageName
#
#         with open(FaName, 'w', encoding='utf-8') as f2:
#             for line in f1.readline():
#                 f2.write(line)
# import  requests
# url='https://csdnimg.cn/public/publick_img/ad_20200515_toolbar80_1.jpg'
# pic=requests.get(url)
# data=pic.content#二进制文件
# with open('pc.jpg','wb') as fp:
#     fp.write(data)
#     print("图片下载完成！")

from turtle import *
color('red','red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()