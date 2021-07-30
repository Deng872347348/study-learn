from  tkinter import *
root=Tk()
li=['C','python','php','html','SQL','java']
moive=['CSS','JQuery','Bootstrap']
listb=Listbox(root)
listb2=Listbox(root)
for item in li:
    listb.insert(0,item)
for item in moive:
    listb2.insert(0,item)

listb.pack()

#进入消息循环
top.mainloop()
