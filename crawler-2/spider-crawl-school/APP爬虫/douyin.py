from appium import  webdriver
import time

class DouyinAction():
    def __init__(self,nums:int=None):
        # 初始化配置，设置Desired Capabilities参数
        self.desired_caps = {
            "platformName":"Android",
            "deviceName":"LIO-AN00",
            "appPackage":"com.ss.android.ugc.aweme",
            "appActivity":".splash.SplashActivity"
        }
        # 指定Appium Server
        self.server = "http://localhost:4723/wd/hub"
        # 新建一个driver
        self.driver = webdriver.Remote(self.server,self.desired_caps)

        # 获取模拟器/手机的分辨率
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()['height']
        print(width,height)
        # 设置滑动初始化和滑动距离
        self.start_x = width//2 # 屏幕宽度中心点
        self.start_y = height//3*2 # 屏幕高度从上开始到下三分之二处
        self.distance = height//2 # 滑动距离：屏幕高度一半的距离
        # 设置滑动的次数
        self.nums =nums

    def comments(self):
        # app开启之后点击一次屏幕，确保页面的展示
        time.sleep(2)
        self.driver.tap([(500,1200)],500)
    def scroll(self):
        print("滑动ing...")
        self.driver.swipe(self.start_x,self.start_y,self.start_x,
                          self.start_y-self.distance)
        time.sleep(3)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]").click()
        time.sleep(3)
        # 无限滑动
        i = 0
        while True:
            # 模拟滑动
            print("滑动ing...")
            self.driver.swipe(self.start_x,self.start_y,
                              self.start_x,self.start_y-self.distance)
            time.sleep(3)
            self.get_infos() # 获取视频发布者的名字
            # 设置延时等待
            time.sleep(4)
            # 判断是否退出
            if self.nums is not None and self.nums == i:
                break
            i += 1
    def get_infos(self):
        # 获取视频的各种信息:使用appium desktop定位元素
        print(self.driver.find_element_by_id("ap").text) # 发布者的名字
        print(self.driver.find_element_by_id("xm").text) # 点赞数
        print(self.driver.find_element_by_id("xn").text) # 留言数
        print(self.driver.find_element_by_id("oz").text) # 视频名字，可能不存在，报错


    def main(self):
        self.comments() # 点击一次，确保页面的展示
        time.sleep(2)
        self.scroll() # 滑动

if __name__ == '__main__':
    action =DouyinAction(nums=5)
    DouyinAction.main()