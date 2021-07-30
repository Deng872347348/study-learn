
#类属性的应用 计数
class Goose:
    number=0 #计数器
    def __init__(self,wings,legs):
        self.wings=wings
        self.legs=legs
        #计数器如何+1
        Goose.number+=1
        print("目前为止大雁一共有"+str(Goose.number)+"只！")
#生成4只大雁
gooselist=[]
for i in range(4):
    gooselist.append(Goose("2只翅膀",2))