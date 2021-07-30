
import threading
import time
def p(a):
    for i in range(1, 100):
        print(i, end=', ')
        time.sleep(1)


def p1(a):
    for i in range(101, 200):
        print(i, end=', ')
        time.sleep(1)


if __name__ == '__main__':

    t11 = threading.Thread(p(1))
    t22 = threading.Thread(p1(2))
    t11.start()
    t22.start()
    t11.join()
    t22.join()