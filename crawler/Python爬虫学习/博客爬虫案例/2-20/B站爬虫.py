#流程
#导入工具
import requests #第三方工具
import re #正则
import csv #处理保存csv文件格式
import jieba #用来分词的国人开发的库 import wordcloud
import imageio # 读图片
import wordcloud #词云库
#
# #目标网站
# url = ' https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=186803402&date=2021-02-17'
# #模拟浏览器发送请求，接受返回的数据
# headers = {
#     # 用户代理 身份证
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
#     # 账号已登录信息
#      'cookie': '_uuid=DB17FC3E-C33B-0402-FEC8-6D5F54FFD75826400infoc; buvid3=524A488F-FA38-4505-A9FD-80539B19E3FB184978infoc; sid=a2zoyf7s; buvid_fp=524A488F-FA38-4505-A9FD-80539B19E3FB184978infoc; DedeUserID=650586683; DedeUserID__ckMd5=673346effe04fe44; SESSDATA=dc4b2c16%2C1628474903%2Cc95da*21; bili_jct=f92980128fe4681476212c6cfe3d0ff7; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(J|)JR|||Rm0J uYukmkkmJk; fingerprint3=dc6c77bb0dfdccdd39bc9efbb780630d; fingerprint=f29725bb59f7984374f945e2ebddc362; buvid_fp_plain=524A488F-FA38-4505-A9FD-80539B19E3FB184978infoc; fingerprint_s=0a7abb581b9ea03451e614a51a3d4b2b; LIVE_BUVID=AUTO8416133069733130; bp_video_offset_650586683=491829482594004200; bsource=search_baidu; PVID=1; bfe_id=1e33d9ad1cb29251013800c68af42315'
# }
# resp = requests.get(url,headers=headers)
# print(resp) # 打印输出一下看是否可以正常访问
# print(resp.text)#以文本的形式打印网页源代码
# # 获取弹幕数据
# #中文
# Danmu = re.findall("[\u4e00-\u9fa5]+",resp.text) # 用到的正则，匹配中文
# print(Danmu)
# # 4.数据保存
# for i in Danmu : #相当于一个遍历保存
#     with open('B站弹幕.csv','a',newline='',encoding='utf-8') as f :
#         writer = csv.writer(f)
#         danmu = []
#         danmu.append(i)
#         writer.writerow(danmu)
# 绘制词云
f = open('B站弹幕.csv','r',encoding='utf-8')
txt = f.read()
#print(txt)

# 1.分词处理
textlist = jieba.lcut(txt)
print(textlist)
string1 = ' '.join(textlist) #拼接成整个字符串
#print(string)
mk = imageio.imread(r'心.jpg')
w=wordcloud.WordCloud(
    width = 1000,
    height =700,
    background_color ='white',
    font_path='msyh.ttc',
    mask =mk,
    scale = 18,
    stopwords = {'','\n','\r'},#停用词
    contour_width =5,
    contour_color ='red'

)
# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string1)
#将词云图片导出到当前文件夹
w.to_file('out1.png')


