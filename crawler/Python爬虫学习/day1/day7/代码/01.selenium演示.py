#pip install selenium
from selenium import webdriver

# 初始化driver环境
driver = webdriver.Chrome()


# 向一个url发起请求
driver.get("https://www.baidu.com/")

# 打印页面标题
print(driver.title)

# 退出浏览器
#driver.quit()  # 一定要记得退出！不然会有残留进程

# from selenium import webdriver
#
# driver = webdriver.PhantomJS()
#
# driver.get("https://www.baidu.com")
#
# # 把网页保存成图片
# driver.save_screenshot('baidu.png')
#
# driver.quit()