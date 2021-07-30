import requests
import time
import os

url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
response=requests.get(url)
response_data=response.json()
print(response_data)
hero_list=response_data['hero']
#path="C:\Users\Lenovo\Desktop\英雄联盟"
path='E:\python社区版\python项目\Python爬虫学习案例\英雄联盟'
for hero in hero_list:
    heroId=hero['heroId']
    heroName=hero['name']+"-"+hero['title']
    print("英雄ID："+heroId)
    print("英雄名称:"+heroName)
    if not os.path.exists(path+heroName):
        os.mkdir(path+heroName)
    hero_info_url="https://game.gtimg.cn/images/lol/act/img/js/hero/"+heroId+".js"
    hero_info_response=requests.get(hero_info_url)
    hero_info_data=hero_info_response.json()
    skins=hero_info_data['skins']
    for skin in skins:
        skin_img_url=skin['mainImg']
        skin_name=skin['name']
        if skin_img_url:
            skin_img_data=requests.get(skin_img_url).content#获取图片文件二进制的数据
        fileName=path+heroName+"/"+skin_name+".jpg"
        with open(fileName,'wb') as f:
            f.write(skin_img_data)
            print(skin_name+".....皮肤图片爬取完毕")

        time.sleep(2)