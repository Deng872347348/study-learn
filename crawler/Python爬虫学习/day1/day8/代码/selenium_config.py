from selenium import  webdriver
import time

url = 'http://www.baidu.com'

# 创建配置对象
opt = webdriver.ChromeOptions()

# 添加配置参数
# 设置浏览器为无头模式
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# # 更换ip代理，必须要重新启动浏览器
# opt.add_argument('--proxy-server=http://60.255.151.82:80')
#
# # 更换user=agent
# opt.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

# 创建浏览器对象的时候添加配置对象
driver = webdriver.Chrome(chrome_options=opt)

driver.get(url)
driver.save_screenshot('百度_.png')

time.sleep(2)
driver.quit()