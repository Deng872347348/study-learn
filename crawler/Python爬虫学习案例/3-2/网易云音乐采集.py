from selenium import webdriver
import MySQLdb
import time
conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'test',
    charset='utf8mb4'
)
cursor = conn.cursor()
# 隐藏浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 给设置 的属性添加headless属性，使浏览器隐藏起来，不弹出。
driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
url = "https://music.163.com/#/song?id=493735012"
driver.get(url)
# 切换到对应的ifame标签里
driver.switch_to_frame('g_iframe')
for i in range(1, 500):
    driver.execute_script("var q=document.documentElement.scrollTop=5000")
    nodes = driver.find_elements_by_xpath('//div[@class="cnt f-brk"]')
    for node in nodes:
        sql = 'insert into wyy values(%s)'
        cursor.execute(sql, [node.text])
        conn.commit()
    a = driver.find_element_by_xpath('//a[text()="下一页"]') # 筛选文本内容为下一页的a标签
    a.click()  # 点击该标签
    time.sleep(1)  # 点击下一页之后休眠两秒，等待页面加载
    print('第{}页评论爬取完成'.format(i))
