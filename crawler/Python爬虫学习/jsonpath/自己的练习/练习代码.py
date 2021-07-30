book_dict = '''{ 
  "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}'''
import json
import  jsonpath
# 取第三本书
data=json.loads(book_dict)
#print(jsonpath.jsonpath(data,"$..bicycle"))
# 去store中的所有的book的作者
#print(jsonpath.jsonpath(data,"$..store.book[*].author"))
# 所有的作者
#print(jsonpath.jsonpath(data,"$..author"))
# store下的所有的元素
#print(jsonpath.jsonpath(data,"$..store"))
#print(jsonpath.jsonpath(data,"$.store.*"))
# store中的所有的内容的价格
# print(jsonpath.jsonpath(data,"$.store.book[*].price"))
#print(jsonpath.jsonpath(data,"$..price"))
# 第三本书
# 最后一本书
#print(jsonpath.jsonpath(data,"$..book[-1:]"))
# 前两本书
#print(jsonpath.jsonpath(data,"$..book[0:2:1]"))
# 获取价格大于10的所有的书
# print(jsonpath.jsonpath(data,"$.store.book[*].price"))
print(jsonpath.jsonpath(data,"$..book[?(@.price<10)]"))
 # 获取所有的数据
# print(jsonpath.jsonpath(data,"$.."))


# jsp='[1,2,3,5,6]'
# print(json.loads(jsp))
#
# strlist='{"city":"上海","邓波":"小北"}'
# print(json.loads(strlist))
#
#
# jsp=[1,2,3,5,6]
# strlist={"city":"上海","邓波":"小北"}
# print(json.dumps(jsp))
# print(json.dumps(strlist))
# json.loads()
# strList = '[1,2,3,4]'
# print(json.loads(strList))
#
# strDict = '{"city":"北京","name":"小猫"}'
# print(json.loads(strDict))
