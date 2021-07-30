import requests
import jsonpath
import urllib.request
import os
# 获取歌曲的详细信息包括链接以及标题
def get_music_name():
    name=entry.get()
    if v.get()==1:
        type='netease'
    elif v.get()==2:
        type='qq'
    elif v.get() == 3:
        type = 'kuwo'
    elif v.get() == 4:
        type = 'kugou'
    params={
        'input':name,
        'filter':'name',
        'type':type,
        'page':1,
    }
    headers={
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',}
    url='http://music.onlychen.cn/'
    response=requests.post(url,data=params,headers=headers)
    data=response.json()
    url=jsonpath.jsonpath(data,'$..url')[0]
    title=jsonpath.jsonpath(data,'$..title')[0]
    download(url,title)

# 下载歌曲
def download(url,title):
    dir_name=r'D:\software\python\python爬虫\vip音乐'
    os.makedirs(dir_name,exist_ok=True)

    path=dir_name+'/{}.mp3'.format(title)
    text.insert(END,'{}正在下载'.format(title))
    text.see(END)
    text.update()

    urllib.request.urlretrieve(url,path)

    text.insert(END, '{}已经下载完毕'.format(title))
    text.see(END)
    text.update()

# 界面制作
from tkinter import *
# 创建一个窗口
root=Tk()
v = IntVar()
v.set(1)
# 添加标题
root.title('全网音乐下载器')
# 修改窗口大小
root.geometry('560x430+400+200')
# 标签组件
label=Label(root,text='输入下载的歌曲名：',font=('黑体常规',20))
label.grid(row=0,columns=2)

entry=Entry(root,font=('黑体常规',20),width=15)
entry.grid(row=0,column=2,columns=2)

Radiobutton(root, text="网易云",variable=v,value=1,width=10).grid(row=1, column=0)
Radiobutton(root, text="qq音乐",variable=v,value=2,width=10).grid(row=1, column=1)
Radiobutton(root, text="酷我",variable=v,value=3,width=10).grid(row=1, column=2)
Radiobutton(root, text="酷狗",variable=v,value=4,width=10).grid(row=1, column=3)

text=Listbox(root,font=('黑体常规',16),width=50,heigh=15)
text.grid(row=2,columns=4)

button1=Button(root,text='开始下载',font=('黑体常规',15),command=get_music_name)
button1.grid(row=3,column=0)

button2=Button(root,text='退出程序',font=('黑体常规',15),command=root.quit)
button2.grid(row=3,column=3)

root.mainloop()
