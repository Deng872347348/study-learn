# password = input()
# if password.isdigit()==True or password.isalpha():
#     print("低级密码")
# elif password.isalnum():
#     print("中级密码")
# else:
#             print("高级密码")
# import string
# password = input()     # 获取密码字符串
# k=string.punctuation
# p=0
# P=0
# P1=0
# P2=0
# for i in password:
#     for j in k:
#         if(i==j):
#             p=1
# L=string.ascii_letters
# for i in L:
#     if(password[0]==i):
#         P=1
# for i in password:
#         if(i.isdigit()):
#             P1=1
# for i in password:
#         if(i.isalpha()):
#             P2=1
# if(len(password)>=8 and p==1 and P2==1 and p==1 and P==1):
#     print("高级密码")
# elif(P1==1 and P2==1):
#     print("中级密码")
# else:
#     print("低级密码")

# import  string
# import  random
# n=int(input())
# str1=string.ascii_letters+string.digits
# result=""
# for i in range(n):
#     result=result+random.choice(list(str1))
#     if result.isalnum() and len(result)==n:
#         print(result)
#         print("验证码生成成功")
#     else:
#         print("验证码生成错误")
# import  string
# import  random
# a=string.ascii_letters
# b=string.digits
# print(a)
# print(b)
# ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
# print (ran_str)
#
# str.isalpha()
# str.isspace()

str1 = input()     # 包含邮箱号的字符串
str2=str1.split(",")
str3=[]
result = []
for i in str2:
 k=i.split("@")[1].split(".")[0]

 str3.append(k)
str3=sorted(list(set(str3)))
for x in str3:
    list2 = []
    for y in str2:  # 遍历所有邮箱
        if (x==y.split("@")[1].split(".")[0]):
            list2.append(y)  ## 如果是x的服务商
    result.append(x+":"+",".join(list2))
print(result)




# import re
# str1 = input()
# str2=re.sub("[A-Za-z0-9!%[],\。\*/]","",str1)
# print(str2)

# import re
# str1="<p>喜**马**拉**雅**山</p>"
# str2=""
# for i in str1:
#     if i.isalpha():
#         str2+=i
# print(str2)
# str3=re.sub("[A-Za-z0-9]","",str2)
# print(str3)