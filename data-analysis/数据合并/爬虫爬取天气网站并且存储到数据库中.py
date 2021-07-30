import requests
import os
from lxml import etree
from fake_useragent import UserAgent

#
# 定义爬取天气网页的url
class weather(object):
  def __init__(self):
      self.url="http://www.tianqihoubao.com/lishi/changsha/month/202001.html"
      self.headers={'User-Agent':str(UserAgent().random)}
    #定义获取响应页面的内容
  def get_url(self):
      response=requests.get(url=self.url,headers=self.headers).text#对网页内容码
      # print(response)
      # print(self.headers)//测试代码的Useaget是否正确
      # print(html)
      return  response
    #对requests获取的响应页面进行数据的解析
  def get_content(self,data):
      #对获取的网页进行xpath解析
      html = etree.HTML(data)
      detail_xpath=html.xpath('//*[@id="content"]')
      print(detail_xpath)
      # for i in detail_xpath:
      #     print(i)
          #获取日期
      date=html.xpath("//table[@class='b']/tbody/tr/td[1]/a/text()")
      print(date)
      #获取天气状况
      weathercondition=html.xpath("//table[@class='b']/tbody/tr/td[2]/text()")
      print(weathercondition)
      #获取气温
      temperature=html.xpath("//table[@class='b']/tbody/tr/td[3]/text()")
      print(temperature)
      #获取风力风向
      Winddirection=html.xpath("//table[@class='b']/tbody/tr/td[4]/text()")
      print(Winddirection)
          # weatherList=[]

  #定义一个函数实现翻页的功能
  # def get_page(self):

  #运行函数
  def run(self):
      data=self.get_url()
      self.get_content(data)
      # page=self.get_page()

#主函数运行

if __name__ == '__main__':
    result= weather()
    result.run()

