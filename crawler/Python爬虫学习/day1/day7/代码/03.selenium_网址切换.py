from selenium import  webdriver

import time

url = 'http://www.baidu.com'
driver = webdriver.Chrome()

driver.get(url)
# time.sleep(2)
# driver.get('https://www.douban.com')
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)

# 浏览器标题
print(driver.title)

# 响应url
print(driver.current_url)

# 渲染之后的源码
print(driver.page_source)

# 截屏
driver.save_screenshot('baidu.jpg')

driver.quit()
