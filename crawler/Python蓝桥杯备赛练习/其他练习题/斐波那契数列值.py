# while True:#异常处理
#     try:
#         n=int(input())#键盘读入
#         F1,F2=1,1
#         for i in range(3,n+1):
#             F1,F2=F2%10007,(F1+F2)%10007#先取余再递推防止超时
#         print(F2)
#     except:
#         break

#A,B=map(int,input().split());print(A+B);

while True:
    try:
        n=int(input())
        if n>=1 and n<=200:
            sl=list(map(int,input().split()))
            sl.sort()#默认reverse=False从小到大输出,reverse=True则相反
            for i in range(len(sl)):
                print(sl[i],end=' ')#end=' '的作用是输出不换行
    except:
        break