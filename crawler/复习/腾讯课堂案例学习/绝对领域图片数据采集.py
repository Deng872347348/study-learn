import requests
from  lxml import etree

def get_url(start_url):
   response=requests.get(start_url)
   data=etree.HTML(response.text)#转化成xpath能处理的对象
   #print(data)
   new_url_list=data.xpath('//div[@class="post-module-thumb"]/a/@href')
   for url in new_url_list:
    res=requests.get(url)
    img_data=etree.HTML(res.text)
   img_url_list=img_data.xpath('//div[@class="entry-content"]//img/@src')
   for img_url in img_url_list:
       #print(img_url)
        file_name=img_url.split("/")[-2]+img_url.split("/")[-1]
        print(file_name)
        result=requests.get(img_url).content
        with open("图片/"+file_name,'wb') as f:
           f.write(result)
           print("正在下载",file_name)



if __name__=="__main__":#python的程序入口
     for i in range(50,78):
         start_url='https://www.jdlingyu.com/tuji/hentai/gctt/page/{}'.format(i)
         get_url(start_url)



# if __name__=="__main__":#python的程序入口
#   for i in range(1,78):
#      start_url='https://www.jdlingyu.com/tuji/hentai/gctt/page/{}'.format(i)
#      response = requests.get(start_url)
#      data = etree.HTML(response.text)  # 转化成xpath能处理的对象
#      new_url_list = data.xpath('//div[@class="post-module-thumb"]/a/@href')
#      for url in new_url_list:
#          res = requests.get(url)
#          img_data = etree.HTML(res.text)
#      img_url_list = img_data.xpath('//div[@class="entry-content"]//img/@src')
#      for img_url in img_url_list:
#          # print(img_url)
#          file_name = img_url.split("/")[-2] + img_url.split("/")[-1]
#          print(file_name)
#          result = requests.get(img_url).content
#          with open("图片/" + file_name, 'wb') as f:
#              f.write(result)
#              print("正在下载", file_name)