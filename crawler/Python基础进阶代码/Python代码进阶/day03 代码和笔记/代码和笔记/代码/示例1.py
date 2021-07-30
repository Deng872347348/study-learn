"""
根据用户输入的内容去查询：
    - 大保健，去搜索股票名称中是否包含`大保健`，如果包含就展示股票。
    - 涨跌额 > 45  or 涨跌额 < 20
# 项目提供的内容：
    1. 文件提供给我们。
    2. 根据用户输入的内容去查询：
        - 大保健，去搜索股票名称中是否包含`大保健`，如果包含就展示股票。
        - 当前价 > 45  or 涨跌幅 < 20
    3. 对于搜索的时候
        - 根据大保健搜索，则只去查找文件的 则只匹配 股票名称
        - 范围 valid_filter_columns = ["当前价", "涨跌幅", "换手率"]

# 系统的实现思路：
    1. 将文件中的数据读取到Python的内存中，以什么样的格式存储？
        - 表头，处理
        - 数据，处理
    2. 用户输入关键字，然后解析关键字。
        - 【大保健】，去内存中找股票名称进行比较。
        - 【当前价 > 45.0 】
            - 检验下 `当前价` 是否支持？ ["当前价", "涨跌幅", "换手率"]
            - 检验下，`45.0` 是不是小数？不是小数则格式错误。
            - 处理是大于还是小于？
                if xx > xx:
                    pass
                else:
                    pass
    3. 准则：
        - 不要出现太多的嵌套 11层嵌套
        - 如果有if else这种条件，一定要把简单的逻辑放在上面。
            if xx:
                100行
            else:
                5行

            if not xx:
                5行
            else:
                100行
"""
import re
import operator

# ################### 1.读取文件到字典 ###################
# 保存所有的股票信息
stock_dict = {}

# 以后做范围查询，只能查这几项。
valid_filter_columns = {"当前价", "涨跌幅", "换手率"}

# 打开文件，文件内容读取到stock_dict中
with open("stock_data.txt") as file_object:
    headers = file_object.readline().strip().split(",")
    for line in file_object:
        line = line.strip().split(",")
        code = line[0]
        stock_dict[code] = line

# ################### 2.用户输入内容然后搜索 ###################
# 关键字：啤酒
# 范围：换手率>9
while True:
    cmd = input("请输入要查询的股票：").strip()
    # 如果是空，则不再继续往下执行，而是重新输入。
    if not cmd:
        print("搜索条件不能为空")
        continue
    # `啤酒`  `xxxx<9`  `xxxx>9` `xxxx<9>9>99<66`

    # `啤酒` 长度 1
    # `xxxx<9` `xxxx>9`  长度2
    # `xxxx<9>9>99<66`  长度大于2
    syntax_parser = re.split("[<>]", cmd)
    if len(syntax_parser) > 2:
        print("输入格式错误，请从新输入。")
        continue

    # 2.1 关键字处理
    if len(syntax_parser) == 1:
        # 查询股票名称
        for code, row in stock_dict.items():
            if cmd in row[1]:
                print(row)
        continue

    # 2.2 处理范围
    # ["市盈率","50" ]
    filter_column, filter_value = syntax_parser

    # ["当前价", "涨跌幅", "换手率"]
    if filter_column not in valid_filter_columns:
        print("不合法得列，请重新输入。")
        continue
    # 50
    try:
        filter_value = float(filter_value)
    except ValueError:
        print("筛选值非数字，请重新输入。")
        continue

    # 大于还是小于的逻辑
    column_index = headers.index(filter_column)
    compare_function = operator.gt
    if "<" in cmd:
        compare_function = operator.lt

    for code, row in stock_dict.items():
        row_real_value = row[column_index].strip("%")
        row_real_value = float(row_real_value)
        if not compare_function(row_real_value, filter_value):
            continue
        print(row)
