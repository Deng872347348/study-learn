a=[[1],[1]]

n=int(input())
for i in range(n-2):
    b=a[-1]
    new=[1]
    for i in range(len(b)-1):
        new.append(b[i]+b[i+1])
    new.append(1)
    a.append(new)

print(a)