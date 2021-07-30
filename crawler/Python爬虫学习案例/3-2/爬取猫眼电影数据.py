# -*- coding: utf-8 -*-
# !/usr/bin/env python
# 猫眼票房：https://piaofang.maoyan.com/dashboard

import datetime
import os
import time
import requests

class PF(object):
    def __init__(self):
        self.url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=173d6dd20a2c8-0559692f1032d2-393e5b09-1fa400-173d6dd20a2c8&riskLevel=71&optimusCode=10'
        self.headers = {
            "Referer": "https://piaofang.maoyan.com/dashboard",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        }

    def main(self):
        '''
        主程序，打印最终结果
        :return:
        '''
        while True:
            # 需在dos命令下运行此文件，才能清屏
            os.system('cls')
            result_json = self.get_parse()
            if not result_json:
                break
            results = self.parse(result_json)
            # 获取时间
            calendar = result_json['calendar']['serverTimestamp']
            t = calendar.split('.')[0].split('T')
            t = t[0] + " " + (datetime.datetime.strptime(t[1], "%H:%M:%S") + datetime.timedelta(hours=8)).strftime(
                "%H:%M:%S")
            print("北京时间:", t)
            x_line = '-' * 155
            # 总票房
            total_box = result_json['movieList']['data']['nationBoxInfo']['nationBoxSplitUnit']['num']
            # 总票房单位
            total_box_unit = result_json['movieList']['data']['nationBoxInfo']['nationBoxSplitUnit']['unit']
            print(f"今日总票房: {total_box} {total_box_unit}", end=f'\n{x_line}\n')
            # print("{:^10}\t{:^23}".format("企业ID", "企业名称"))
            print('电影名称'.ljust(14), '综合票房'.ljust(11), '票房占比'.ljust(13), '场均上座率'.ljust(11), '场均人次'.ljust(11),
                  '排片场次'.ljust(12),
                  '排片占比'.ljust(12), '累积总票房'.ljust(11), '上映天数', sep='\t', end=f'\n{x_line}\n')
            for result in results:
                print(
                    result['movieName'][:10].ljust(9),  # 电影名称
                    result['boxSplitUnit'][:8].rjust(10),  # 综合票房
                    result['boxRate'][:8].rjust(13),  # 票房占比
                    result['avgSeatView'][:8].rjust(13),  # 场均上座率
                    result['avgShowView'][:8].rjust(13),  # 场均人次
                    result['showCount'][:8].rjust(13),  # '排片场次'
                    result['showCountRate'][:8].rjust(13),  # 排片占比
                    result['sumBoxDesc'][:8].rjust(13),  # 累积总票房
                    result['releaseInfo'][:8].rjust(13),  # 上映信息
                    sep='\t', end='\n\n'
                )
                break # 把break注释掉，打印的是所有电影实时票房,否则只打印榜首

            time.sleep(4)

    def get_parse(self):
        '''
        网页是否成功获取,频繁操作会有验证
        :return:
        '''
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                # print("success!")
                return response.json()
        except requests.ConnectionError as e:
            print("ERROR:", e)
            return None

    def parse(self, result_json):
        '''
        获取数据
        :return:
        '''
        if result_json:
            movies = result_json['movieList']['data']['list']
            # movies = [{},{},{}]
            # 场均上座率, 场均人次, 票房占比, 电影名称,
            # 上映信息（上映天数）, 排片场次, 排片占比, 综合票房,累积总票房
            ticks = ['avgSeatView', 'avgShowView', 'boxRate', 'movieName',
                     'releaseInfo', 'showCount', 'showCountRate', 'boxSplitUnit', 'sumBoxDesc']
            for movie in movies:
                self.piaofang = {}
                for tick in ticks:
                    # 数字和单位分开需要join
                    if tick == 'boxSplitUnit':
                        movie[tick] = ''.join([str(i) for i in movie[tick].values()])
                    # 多层字典嵌套
                    if tick == 'movieName' or tick == 'releaseInfo':
                        movie[tick] = movie['movieInfo'][tick]
                    if movie[tick] == '':
                        movie[tick] = '此项数据为空'
                    self.piaofang[tick] = str(movie[tick])
                yield self.piaofang


if __name__ == '__main__':
    pf = PF()
    pf.main()
