import tkinter as tk  # 创建一个可视化界面程序
import re
#import _tkinter as tkm
# 设置签名的功能函数
import requests


def func():
    # 冲输入框获取名字
    name = entry.get()
    print(name)


url = 'http://m.uustv.com/'
# 设置签名的样式
data = {'word': 'name', 'size': '60', 'fonts': '1.ttf'}

# 请求网站
response = requests.post(url, data).text
# print(response)
img_url = re.findall('<img src="(.*?)"/></div>', response)[0]
print(img_url)
# 找到图片地址
img_path = url + img_url
# 请求图片地址
img = requests.get(img_path)
with open("我的签名照片.jpg", 'wb') as f:
    f.write(img.content)
#tkm.showinfo("提示，签名成功")

# 创建可视化界面
window = tk.Tk()

window.title('个性签名')
window.geometry('400x200')

# 添加需要的的控件
# 输入框
entry = tk.Entry(window, font=('黑体', 16))
entry.place(x=200, y=50, width=150, height=30)

# 提示框
label = tk.Entry(window, text='请输入名字', font=('黑体', 16))
label.place(x=50, y=50, width=150, height=30)

# 按钮
Button = tk.Entry(window, text='设计签名', font=('黑体', 16),command=func())
Button.place(x=70, y=120, width=150, height=30)

# 让界面显示
window.mainloop()
