import tkinter as tk#图形界面库
import tkinter.filedialog as tkf #打开对话框
import pyttsx3

#from tkinter #对话框
#关联相关功能的函数
def select_file():#读取选择的记事本的文字内容
    global book_text
    book_text=''
    path=tkf.askopenfilename()#获取文件路径
    with open(path,'r',encoding='uft-8') as file:
         book_text=file.read()
    text.insert('end',book_text)
#把文字转化成为声音
def broadcast_text():
    book=pyttsx3.init()  #创建一个可以说话的对象，命名为Book
    book.say(book_text)  #设置说话的内容
    book.runAndWait() #开始说话
#创建图形界面窗口
window=tk.Tk() #创建图形界面窗口
#设计窗口的外观
window.title('懒人听书')#设置窗口名字
window.geometry('640x480')#设置窗口默认大小
text=tk.Text(window)  #添加文本框道窗口上
text.place(x=20,y=20,width=600,height=400)

text=tk.Button(window,text='选择数据',command=select_file)  #添加按钮
text.place(x=100,y=430,width=150,height=30)
text=tk.Button(window,text='开始听书',command=broadcast_text)  #添加按钮
text.place(x=350,y=430,width=150,height=30)
window.mainloop()#执行









