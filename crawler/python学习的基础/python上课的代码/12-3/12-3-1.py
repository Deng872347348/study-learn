# with open('八不准.txt','r',encoding='utf-8') as f1:
#     print(f1.read())
#     content=f1.read()
#     f1.close()
#     txt_dict={}
#     for word in content:
#         txt_dict[word]=txt_dict.get(word,0)+1
#     del txt_dict[' ']
#     del txt_dict[' \n']
#     ls=[]
#     for i in txt_dict.keys():
#         ls.append('{0}:{1}'.format(t,txt_dict[t]))
#     with open('八不准.txt','w',encoding='utf-8') as f:
#         f.write(','.join(ls))
#     print('ok')
import  csv
#写入csv文件
#假设你在招聘网上爬取两条数据
from urllib3.filepost import writer

header = ['公司', '招聘职位', '薪资']
data = [
    ['三一重工', '大数据分析师', 6000],
    ['华为', 'Java开发师', 9000]

]
with open('recuit.csv','w',encoding='utf-8',newline='') as fp:
    writer-csv.writer(fp)
    writer .writerow(header)
    writer.writerows(data)
    print("csv下载完毕！")