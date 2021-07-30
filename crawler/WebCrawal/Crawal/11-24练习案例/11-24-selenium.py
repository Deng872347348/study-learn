# selenium模块的基本使用
# 问题：selenium模块和爬虫之间具有什么关联
#    便捷的获取网站中动态加载的数据
#    便捷实现模拟登录
#    什么是selenium模块
#    基于浏览器自动化的一个模块
#    selenium的使用
#    环境安装：pip install selenium
# 下载一个浏览器的驱动程序
#   下载


# 实例化一个浏览器对象
# 编写基于浏览器自动化的操作代码
#   发起请求，get(url)
# 标签定位：find系列的方法
# 标签交互：send_keys('xxx')
# 执行js程序：execute_script('jsCode')
# 前进，后退:back(),forward()
# 关闭浏览器：quit()
# selenium处理iframe
#   如果定位的标签存在iframe标签中，则必须使用switch_to.frame(id)
# 动作链（拖动）from selenium.webdriver import  ActionChains
# click_and_hold(div):长按且点击操作
# move_by_offset(x,y)
# perform()让动作链立即执行
# action.release()释放动作链对象

# from  selenium import webdriver
# from bs4 import BeautifulSoup
# from time import sleep
# from  lxml import etree
# #实例化一个浏览器对象
# bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# #发起一个get请求
# bro.get(url='https://125.35.6.84:81/xk/')
# #获取当前浏览器页面的源码数据
# page_text = bro.page_source
# #使用xpath进行解析
# tree =etree.HTML(page_text)
# dl_list = tree.xpath('//ul[@id="gzlist"]/li')
# for dl in dl_list:
#     name = dl.xpath('./dl/@title')[0]
#     print(name)
# sleep(5)
# bro.quit()

# from  selenium import  webdriver
# from  time import  sleep
# bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# bro.get('https://uland.taobao.com/')
# #标签定位
# search_input=bro.find_element_by_id('q');
# #标签定位
# search_input.send_key('Iphone')
#
# #执行一组js程序
# bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# sleep(2)
# #点击搜索按钮
# btn=bro.find_element_by_css_selector('.btn-search')
# btn.click()
# bro.get('https://www.baidu.com')
# sleep(2)
# #回退
# bro.back()
# sleep(2)
# #前进
# bro.forward()
# bro.quit()


#动作链
#action=ActionChains(bro)
