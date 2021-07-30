# 1.减少判断的代码


def login():
    pass


def register():
    pass


def reset_password():
    pass


map_info = {
    '1': login,
    '2': register,
    '3': reset_password,
}

while True:
    choice = input("请输入：")  # 1/2
    func = map_info.get(choice)  # login、register; 3
    if not func:
        print("输入错误")
        continue
    func()

"""
choice = input("请输入：") # 1、登录；2、注册。
if choice == '1':
    login()
elif choice == '2':
    register()
"""
