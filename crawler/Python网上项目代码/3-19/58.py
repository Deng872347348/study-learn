import csv
import random
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# options = webdriver.ChromeOptions()
# options.set_headless()
# options.add_argument('--diable-gpu')
driver = webdriver.Chrome()
wait_time = WebDriverWait(driver,10,0.5)
# 这里设置隐式等待的时间
# 设置无头Chrome进行作业
# 直接定位到要爬取的网页，不用有一个过程的

#driver.get_screenshot_as_file('58.png')
# 截屏

#get_html = driver.find_element(By.TAG_NAME, 'html')
# 定位到这个get_html元素

def parse_dom(driver,writer):
    content = driver.page_source.encode('utf-8')
    # 获取页面资源
    Soup = BeautifulSoup(content,'lxml')
    # 用BeautifulSoup库进行解析，结合BeautifulSoup
    li_list = Soup.find(attrs={'class':'content'}).find_next(attrs={'class':'listUl'}).find_all('li')
    # 解析
    for li in li_list:
        try:
            if li.has_attr('logr'):
                # 因为渲染过的页面上还有一种公寓的信息，是我不要的，这里的这个判断语句相当于一个赛选
                img_list = li.div.find_next('img').get('src')
                img_num = li.find_next('span').get_text()
                des = li.find(attrs={'class': 'des'})
                h2 = des.h2.a.get_text()
                room = des.find(attrs={'class': 'room'}).get_text()
                jjr = des.find(attrs={'class': 'jjr'}).get_text(strip=True)
                listliright = li.find(attrs={'class': 'listliright'})
                sendtime = listliright.find(attrs={'class': 'sendTime'}).get_text()
                money = listliright.find(attrs={'class': 'money'}).get_text()
                writer.writerow([img_list, img_num, h2, room, jjr, sendtime, money])
            else:
                continue
        except AttributeError:
            continue
        # 有错误什么的都进跳过
    try:
        next_element = wait_time.until(EC.element_to_be_clickable((By.CLASS_NAME,'next')))
        # 定位到页面的“下一页”的按钮，并进行点击
        next_element.click()
        # 点击过后，driver对象就是下一页的内容了，这里不要纠结
        # 注意：在某些时候，点击一个按钮会出现一个新的窗口，这是就要注意切换窗口了。
        driver.get_screenshot_as_file('D:/selenium/{name}.png'.format(name=random.uniform(0,39)))
        # 别问我这个39什么意思，什么意思也没有，我就是随便选的
        # uniform是选取浮点数，如果你想用整数可以用randint
        # 截频每次爬取的网页，并随机生成一个图片的名字
        print(1)
        # 这是我给自己视觉上的一个信号，不然我不知道它在爬取呀！！！！！
        parse_dom(driver,writer)
        # 进行一个递归的循环
    except NoSuchElementException:
        print('已经到了末尾了！')
        return
    # 到了末尾自然就找不到“下一页”那个元素了，这是就可以报错了
    # 就可以return，停止运行了

def main():
    driver.get(url='http://bj.58.com/chuzu/?PGTID=0d200001-0000-1fd1-f53b-dedf284b5de1&ClickID=1')
    with open('58city.csv','a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['img_list', 'img_num', 'h2', 'room', 'jjr', 'sendtime', 'money'])
        # 建立一个writer对象并写入title
        parse_dom(driver,writer)
        # 这个函数我实现的是一个递归的调用

if __name__ == '__main__':
    main()
    # 执行主函数