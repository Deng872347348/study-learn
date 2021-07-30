# def square(x):
#     return x**2
#
# square=lambda x:x**2
# square(2)
# print(square(3))
#
#
# compare=lambda  x,y: x if x>y else y
# print(compare(2,3))
# def square(x) :            # 计算平方数
#     return x ** 2
# print(list(map(square,[1,2,3,4,5,6,7,8,9,10])))
# print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))

# 高阶函数练习题：
# (1)tp = ('TOM', 'lilei', 'JAck', 'hanmeiMeI')
# 得到列表(所有元素的首字母大写)
# (2) #将整数元素的序列，转为字符串型
# #[1，2，3，4] --》[“1”，“2”，“3”，“4”]
# (3)将爱好为“无”的数据剔除掉
# data= [["姓名","年龄","爱好"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]
# (4)打印2010到2019之内的闰年
# (5)把序列[1, 3, 5, 7, 9]变换成整数13579
#tp = ('TOM', 'lilei', 'JAck', 'hanmeiMeI')

#打印2010到2019之内的闰年
# a = filter(lambda x: x % 2 == 0, range(10))
# print(list(a))
# data= [["姓名","年龄","爱好"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]
# b=filter(lambda x:x[0]!='无'and x[1]!='无'and x[2]!='无',data)
# print(list(b))
# b=filter(lambda x:x[0]!='无'and x[1]!='无'and x[2]!='无',data)
# print(list(b))
# da=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2018,2019]
# newlist = filter(lambda x:  x%4==0  , da)
# print("闰年有%s"%(list(newlist)))
#print(newlist)
# new=map(lambda x,y:x*10+y,[1, 3, 5, 7, 9])
# print(list(new))

# from functools import reduce
# def add(x, y):
#      return x*10+y
# a=reduce(add, [1, 3, 5, 7, 9])
# print(a)

# a=map(str,[1,2,3,4])
# print(list(a))
# tp = ('TOM', 'lilei', 'JAck', 'hanmeiMeI')
# pp= list(map(lambda x: x[0].upper() + x[1:].lower(), tp))
# print(list(pp))


# data= [["姓名","年龄","爱好"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]
# b=filter(lambda x:False if x[-1]!='无' else True,data)
# print(list(b))

# data= [["姓名","年龄","爱好"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]
# def f(liste1):
#     for i in liste1:
#         if i=='无':
#             return False
#
#     return True
# b=list(filter(f,data))
# print(b)

# key = input()
# p = int(input())
# for i in key:
#     if 'A'<=i<='Z':
#         print(chr(ord(i)+p),end='')
#     elif 'a'<=i<='z':
#         print(chr(ord(i)+p),end='')
#     else:
#         print(i,end='')

# print([i for i in range(2010,2050) if i%4==0 or i%400 and i%100==0])

# def study_time(time):
#     time=0
#     def insert_time(min):
#         nonlocal time
#         time=time+min
#         return time
#     return  insert_time
# f=study_time(0)
# print(f(0))
# print(f(10))
# print(f(100))

