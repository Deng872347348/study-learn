# enconding:utf-8

import requests
import pandas as pd
import os
import random
from concurrent.futures import ThreadPoolExecutor
import threading

read_info = pd.read_csv('down_data8-1.csv', low_memory=False)  # 读取数据文件
df_info = pd.DataFrame(read_info)
csv_downurl = df_info['downurl']  # csv 的下载链接
csv_filapath = df_info['filepath']  # csv 的下载路径
downurl_list = csv_downurl.values.tolist()

GLOCK = threading.Lock()


def download():
    while True:
        GLOCK.acquire()
        if len(downurl_list) == 0:
            GLOCK.release()
            break
        downurls = downurl_list.pop()
        GLOCK.release()

        newpd = df_info[str(downurls) == csv_downurl]
        img_down_path = newpd['filepath'].values[0]  # 下载本地路径

        if os.path.isdir("CARINFO/%s" % img_down_path):
            try:
                requ = requests.get(downurls)
            except:
                with open("未下载连接.txt", 'a+', encoding='utf-8') as k:
                    k.write(downurls+'\n')
                    k.close()
            else:
                print("下载：", downurls)
                with open("已下载URL.txt", 'a+', encoding='utf-8') as k:
                    k.write("%s+%s\n"%(downurls,img_down_path))
                    k.close()
                number = random.sample(range(1, 10000000), 1)[0]
                random_name = str(random.sample(range(1000000, 100000000), 1)[0]) + str(number)  # 图片名称

                # name = 'https://i.fuelapi.com/0051aa8a0d4840758d72629ff2967036/758/1/11/stills_0640/MY2002/1145/1145_st0640_081.jpg'

                filename1 = str(downurls).split('/')[-1].split('.')[0] + random_name
                filename2 = str(downurls).split('/')[-8:-1]
                filename3 = ''.join(filename2) + filename1

                with open("CARINFO/%s/%s.jpg" % (img_down_path, filename3), 'wb') as m:
                    m.write(requ.content)
                    m.close()
        else:
            try:
                os.makedirs("CARINFO/%s" % img_down_path)
            except:
                pass


if __name__ == '__main__':
    for x in range(200):  # 修改数字可以增加线程
        th = threading.Thread(target=download)
        th.start()