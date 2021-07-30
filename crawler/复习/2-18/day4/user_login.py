# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

# 1. 确定 在文件 里存储的账号信息的结构

# 2. 把账号数据读到内存，为了方便调用 ，可以改list
accounts = {
    # "alex":["alex","abc123!","1"],
}
f = open("account.db", "r")
for line in f:
    line = line.strip().split(",")
    accounts[line[0]] = line
print(accounts)
# 3. 搞个loop , 要求用户输入账号信息， 去判断 就可以了

while True:
    user = input("Username:").strip()
    if user not in accounts:  # 用户未注册
        print("该用户未注册...")
        continue
    elif accounts[user][2] == "1": # 代表此账户已锁定
        print("此账户已锁定,请联系管理员..")
        continue
    count = 0
    while count < 3:  # 控制密码
        passwd = input("Password:").strip()
        # 去账号dict里去判断password对不对
        if passwd == accounts[user][1]:
            print(f"Welcome {user}...登录成功...")
            exit("bye...")
        else:
            print("Wrong password.....")

        count += 1

    if count == 3:
        print(f"输错了{count}密码，需要锁定账号{user}...")
        # 1. 先改在内存中dict账号信息的 用户状态
        # 2. 把dict里的数据转成原account.db数据格式，并且 存回文件
        accounts[user][2] = "1"
        f2 = open("account.db", "w")
        for user,val in accounts.items():
            line = ",".join(val) + "\n" # 把列表再转成字符
            f2.write(line)
        f2.close()

        exit("bye.")