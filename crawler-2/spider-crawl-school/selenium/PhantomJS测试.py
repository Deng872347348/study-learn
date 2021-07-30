from selenium import  webdriver

driver=webdriver.PhantomJS()

driver.get("http://www.baidu.com/")

#操作输入框，先定位输入框
driver.find_element_by_id('kw').send_keys('python')
#点击事件
button_tag=driver.find_element_by_id('su')
button_tag.click()
#查看当前请求的url地址
print(driver.current_url)
#截屏
driver.save_screenshot('baidu2.png')