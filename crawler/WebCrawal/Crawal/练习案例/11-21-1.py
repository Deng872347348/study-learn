# import  requests
# if __name__=="__main__":
#     url=""
#     kw=input("enter a word:")
#     param={
#         'query':kw
#     }
#     #对指定的url发起的请求对应的url是携带参数的并且请求过程中处理了参数
#     response=requests.get(ur=url,params=param)
#     page_text=response.text
#     fileName=kw+'.html'
#     with open(fileName,'w',encoding='utf-8') as fp:
#         fp.write(page_text)
#         print(fileName,"保存成功！！！")
l=1.02**365
print(l)