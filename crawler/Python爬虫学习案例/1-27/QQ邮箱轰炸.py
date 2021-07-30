import  time
from  pynput.mouse import  Button
from pynput.mouse import  Button,Controller as mouse_cl
from  pynput.keyboard import  Key,Controller as key_cl #键盘控制器

def send_message():
     #先定位到输入框的位置，利用鼠标左键的点击来实现
      mouse=mouse_cl() #获取鼠标的控制权限
      mouse.press(Button.left) #模拟鼠标左键的按下，点击事件，按下，松开
      mouse.release(Button.left)#模拟鼠标左键的松开

     # 用来控制发送次数range范围：
      for i in range(5):
      # 在输入框输入文字
        keyboard = key_cl()  # 获取键盘的控制权限
        keyboard.type("打卡，提醒你们每天打卡")  # 设置发送内容
        # 发送方式，程序按下回车键发送消息一一条消息
        keyboard.press(Key.enter)  # 模拟键盘回车键的按下
        keyboard.release(Key.enter)  # 模拟键盘回车键的松开
      #在输入框中输入文字
      # keyboard=key_cl() #获取键盘的控制权限
      # keyboard.type('打卡，提醒你们每天打卡')#设置发送内容
      # #发送发送，程序按下回车键发送消息，一条消息
      # keyboard.press(Key.enter) #模拟键盘回车键的按下
      # keyboard.release(Key.enter)#你好，你好
# 模拟键盘回车键的松开
      time.sleep(1) #休息3秒钟
#调用函数
send_message()


