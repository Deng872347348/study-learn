from selenium import  webdriver
import time

driver=webdriver.Chrome()

url='https:www.baidu.com'
driver.get(url)
# driver.quit()

#print(driver.title)
#响应的url
# print(driver.current_url)
# #
# # #打印渲染后的源码
# print(driver.page_source)
# #
# # #截图
# driver.save_screenshot('baidu.jpg')
# driver.quit()

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('电影票房')
driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.quit()