# coding:utf-8
import jsonpath
import json

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

data = json.loads(book_dict)

# print(jsonpath.jsonpath(data,"$..color")) # 取颜色
#
#print(jsonpath.jsonpath(data,"$..author")) # 取所有的记者

#print(jsonpath.jsonpath(data,"$store.book[*].author")) # 绝对路径取所有的作者名
#
#print(jsonpath.jsonpath(data,"$..book[2]")) # 取第三本书
#
#print(jsonpath.jsonpath(data,"$..book[@.length-1]|$..book[-1:]")) # 取最后一本书

#print(jsonpath.jsonpath(data,"$.store.*")) # 取所有的元素