import requests
import re
import base64
base_url="https://news.sina.cn/zt_d/yiqing0121"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
response = requests.get(url=base_url,headers=headers)
content = response.text
# print(content)
# 提取base64加密的字符串
resp=r'(base64,(.*?)/)'
sp=re.findall(resp,content)

print(sp)
str = base64.b64decode(sp).decode()
# base64编码后的二进制图片文件
print(str)
# # base64解码(解成二进制串)


# resp=r'(base64,(.*?)/)'
# sp=re.findall(resp,html,re.S)
# print(sp[0])

# # 将字符串 base64_str 用 base64 进行解密
# base64_str = b'RWR1Q29kZXI='
# import base64 # 导入 base64 库
# str = base64.b64decode(base64_str).decode()
# print(str) # 输出结果为：EduCoder
# 写入jpg文件



# base64 加密：
#
# # 将字符串 str 用 base64 进行加密
# str = "EduCoder"
# import base64 # 导入 base64 库
# # 想将字符串转编码成 base64,要先将字符串转换成二进制数据
# bytes_str = str.encode("utf-8")
# base64_str = base64.b64encode(bytes_str)  # b64encode() 函数可以经二进制数据进行加密，被编码的参数必须是二进制数据
# print(base64_str) # 输出结果为：b'RWR1Q29kZXI='
# base64 解密：
#
# # 将字符串 base64_str 用 base64 进行解密
# base64_str = b'RWR1Q29kZXI='
# import base64 # 导入 base64 库
# str = base64.b64decode(base64_str).decode()
# print(str) # 输出结果为：EduCoder


