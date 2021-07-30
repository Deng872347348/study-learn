"""
技术角度：

    # 判断是不是豹子
    def func1():
        pass

    # 判断是否同花
    def func2():
        pass

    # 判断是不是对子
    def func3():
        pass


    func_list = [func1, func2, func3]

    # 三张牌
    for item in func_list:
        result = item()
        if result:
            break


    ----> 通过上述过程可以判断出 牌 到底是啥？  判断牌的大小？
        思路A：
            豹子 + 10000  -> 分值（大小比较）
                10002
                10003
                10004
            同花顺 + 5000
                5001
            对子 + 2000
            单点
        思路B：（源码&计算机底层） 三张牌
            豹子：  6 xx 00 00  # 6 14 00 00   6 13 00 00  6 13 00 00
            同花顺：5 xx 00 00
            同花：  4 xx xx xx  # 4 09 07 03   4 09 07 05
            顺子：  3 xx 00 00
            对子：  2 xx xx 00
            单点：  1 xx xx xx

        研究websocket、socket协议等源码（二进制位）。


"""