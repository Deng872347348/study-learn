
import tkinter as tk#图形界面库
import tkinter.filedialog as tkf #打开对话框
import webbrowser
#实现VIP视频破解
def player():
    video_url=entry.get()
    vip_url=''#破解VIP视频的接口
    webbrowser.open(vip_url+video_url)
#创建图形界面窗口
window=tk.Tk() #创建图形界面窗口
#设计窗口的外观
window.title('VIP破解视频')#设置窗口名字
window.geometry('350x150')#设置窗口默认大小

#在图形窗口
label=tk.Label(window,text='VIP视频的地址:')
label.place(x=20,y=20,width=90,height=30)

entry=tk.Entry()
entry.place(x=120,y=20,width=200,height=30)

button=tk.Button(window,text='VIP视频的地址:',command=player())
button.place(x=80,y=100,width=220,height=30)
window.mainloop()
