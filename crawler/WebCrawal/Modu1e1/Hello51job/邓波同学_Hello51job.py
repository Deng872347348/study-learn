#引入库文件
import requests
import  re
#构建基础的url
word=input("请输入搜索关键字")
base_url="https://search.51job.com/list/000000,000000,0000,00,9,99,"+word+",2,"
end_url=".html"
#构建伪请求头
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'

}
#构建param参数
param={
"lang":"c","postchannel":"0000","workyear":"99","cotype":"99","degreefrom":"99","jobterm":"99","companysize":"99","ord_field":"0","dibiaoid":"0","line":"","welfare":""
}
#循环获取页内容，并持久化
end_page=input("请输入结束页")
for page in range(1,int(end_page)+1):
#构造完整的URL
    url=base_url+str(page)+end_url
#发送HTTP请求
response=requests.get(url,params=param,headers=header)
#获取响应数据
html=response.content.decode("GBK")
#获取数据解析：获取职位信息
pattren=r'class="t1 ".*?<a target=" _blank" title="(.*?)" href="(.*?)>.*?'
content=re.findall(pattren,html,re.S)
#存储
for value in content :
    print(value)
    with open("51.job.txt","a") as file :
        file.write(str(value)+"\n")
        print(value)