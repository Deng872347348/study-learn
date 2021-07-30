import time
import json
from selenium import webdriver
class DouyuSpider(object):
  def __init__(self):
    self.start_rul = 'https://www.douyu.com/directory/all'
    self.driver = webdriver.Chrome()

  def get_content_list(self):
    time.sleep(10) # 强制等待10秒，否则可能报错
    li_list = self.driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li')
    content_list = []
    for li in li_list:
      item = {}
      item['room_img'] = li.find_element_by_xpath('.//img[@class="DyImg-content is-normal "]').get_attribute('src')
      item['room_title'] = li.find_element_by_xpath('.//h3[@class="DyListCover-intro"]').text
      item['root_category'] = li.find_element_by_xpath('.//span[@class="DyListCover-zone"]').text
      item['author_name'] = li.find_element_by_class_name('DyListCover-user').text
      item['watch_num'] = li.find_element_by_class_name('DyListCover-hot').text
      content_list.append(item)
      print(item) # 打印每次获取到的直播房间的信息
    # 获取下一页的元素,为了防止没有报错，这里用elements，翻到最后一页一定就没有了，返回一个列表
    next_url = self.driver.find_elements_by_xpath('//li[@class=" dy-Pagination-next"]')
    next_url = next_url[0] if len(next_url) > 0 else None
    return content_list, next_url
  def save_content_list(self, content_list):
      with open("douyu.txt", "a",encoding='utf-8') as f:
       for content in content_list:
          json.dump(content, f, ensure_ascii=False, indent=2)
          f.write("\n")
          print("保存数据成功")
       f.close()

  def run(self): # 实现主要逻辑
    # 1.start_url
    # 2.发送请求，获取响应
    self.driver.maximize_window()
    self.driver.get(self.start_rul)
    # 3.提取数据，提取下一页的元素
    content_list, next_url = self.get_content_list()
    # 4.保存数据
    self.save_content_list(content_list)
    # 4.点击下一页元素，循环
    while next_url is not None:
      next_url.click()
      content_list, next_url = self.get_content_list()
      self.save_content_list(content_list)
if __name__ == '__main__':
  douban = DouyuSpider()
  douban.run()