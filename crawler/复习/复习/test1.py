# n = int(input())
#
# with open("test.txt") as file_object:
#    content=file_object.readlines()
#    ss=content[0:n]
#    for line in ss:
#        print(line.rstrip())

n = int(input())
list1=[]
with open("test.txt") as file_object:
    for line in file_object:
        list1.append(line.rstrip())

for i in list1[0:n]:
    print(i)