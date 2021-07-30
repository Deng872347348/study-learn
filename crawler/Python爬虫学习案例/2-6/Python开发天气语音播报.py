import pyttsx3
import requests
from lxml import etree


def main():
    url='http://www.weather.com.cn/index/zxqxgg1/jtqxyb.shtml'
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.150Safari / 537.36'
    }
    response=requests.get(url,headers).content.decode()
    #print(response)
    tree=etree.HTML(response)
    list=tree.xpath('//div[@class="rightContent"]/div[@class="graphic"]/div[@class="pageContent"]/p')
    for a in list:
        weather_text=a.xpath('.//text()')
        weather_text=''.join(weather_text)
        #print(weather)

        # 将语音文本说出来
        weather = pyttsx3.init()  # 初始化
        weather.say(weather_text)
        weather.runAndWait()
if __name__ == '__main__':
    main()



