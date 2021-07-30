from selenium import  webdriver
import time
# 1.创建浏览器对象
driver = webdriver.Chrome()

# 2.操作浏览器对象
driver.get('http://www.baidu.com')

# 2.定位元素
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python37')
# driver.find_element_by_id('kw').send_keys('python37')
# driver.find_element_by_name('wd').send_keys('豆瓣')

# 通过class属性值进行元素定位
# driver.find_element_by_class_name('s_ipt').send_keys('阿星')
# driver.find_element_by_css_selector('#kw').send_keys('宗闯')

# driver.find_element_by_xpath('//*[@id="su"]').click()


# print(driver.find_element_by_tag_name('title'))  #根据标签名获取元素列表

# 链接文本(链接和文本在同一个标签中) 通过含有链接的完整文本内容进行元素定位
# driver.find_element_by_link_text('hao123').click()
# 局部的模糊操作
driver.find_element_by_partial_link_text('hao').click()
time.sleep(2)
driver.quit()