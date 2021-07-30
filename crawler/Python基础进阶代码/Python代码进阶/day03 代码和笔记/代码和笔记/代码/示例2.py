import re

# ################### 1.读取文件到字典 ###################
stock_dic = {}

# 变量名，见名知意。
f = open("stock_data.txt")

headers = f.readline().strip().split(",")
print(headers)
for line in f:
    line = line.strip().split(",")
    stock_dic[line[0]] = line
f.close()
valid_filter_columns = ["当前价", "涨跌幅", "换手率"]

print(stock_dic)
# ################### 2.用户输入内容然后搜索 ###################
# 关键字：啤酒
# 范围：换手率>9
while True:
    cmd = input("输入要查询的股票:").strip()
    if not cmd:
        continue
    match_count = 0
    print(headers)

    # 2.1 查询关键字
    for sid, s_data in stock_dic.items():
        s_name = s_data[1]
        if cmd in s_name:
            print(s_data)
            match_count += 1

    # 语法解析 ： 当前价>10
    # step 1. 判断 要查询的列合法
    # step 2. 判断 运算符号右边的值合法
    # step 3. 拿到要查询的列名对应的索引值
    # 2.2 处理范围
    syntax_parser = re.split("[<>]", cmd)

    if len(syntax_parser) == 2:  # 基本合法
        filter_col, filter_val = syntax_parser
        if filter_col in valid_filter_columns:  # 合法列
            filter_val = float(filter_val)  # 有可能报错
            filter_col_index = headers.index(filter_col)  # step 3
            for sid, s_data in stock_dic.items():
                filter_real_val = s_data[filter_col_index].strip("%")
                filter_real_val = float(filter_real_val)  # 有可能报错
                if ">" in cmd:
                    if filter_real_val > filter_val:  # 当前价>10
                        print(s_data)
                        match_count += 1
                if "<" in cmd:
                    if filter_real_val < filter_val:  # 当前价<10
                        print(s_data)
                        match_count += 1
        else:
            print("不合法的查询列.")

    if match_count > 0:
        print(f"匹配到{match_count}条.")
