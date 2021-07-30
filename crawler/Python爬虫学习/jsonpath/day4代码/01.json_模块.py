import  json
import chardet   # 字符串编码  非常优秀的编码识别模块  pip

# json.loads()
# strList = '[1,2,3,4]'
# print(json.loads(strList))
#
# strDict = '{"city":"北京","name":"小猫"}'
# print(json.loads(strDict))


# json.dumps
# listStr = [1,2,3,4]
#
# dictStr = {"city":"北京","name":"大猫"}
#
#
# print(json.dumps(listStr))
# # print("listStr的类型:"+ str(type(listStr)))
# print(chardet.detect(json.dumps(listStr).encode()))
#


# json.dump 使用方法

# listStr = [{"city":'北京'},{"name":"大牛"}]
# print(json.dump(listStr,open("listStr.json",'w'),ensure_ascii=False))
# listStr=[{"city":'北京'},{"name":"大牛"}]
# print(json.dump(listStr,open("listStr.json",'w'),ensure_ascii=False))
# strDict = {"city":'北京'},{"name":"大牛"}
# print(json.dump(strDict,open("strDict.json",'w'),ensure_ascii=True))
#
# # json.load() 使用方法
# strList = json.load(open("listStr.json"))
# print(strList)