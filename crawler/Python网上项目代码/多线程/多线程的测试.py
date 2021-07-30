import threading
import time
def listening():
    for i in range(5):
        print("我在听歌")
        time.sleep(1)
def reading():
    for i in range(5):
        print("我比较喜好")
        time.sleep(1)
if __name__ == '__main__':
    t1=threading.Thread(target=listening())
    t2=threading.Thread(target=reading())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("程序正在运行")
