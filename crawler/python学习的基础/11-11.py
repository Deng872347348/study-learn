#正则的分组


import re
string='<div><a href="#">星期一</a></div>'
result=re.search(r'(<a.*>)(.*)(<\/a>)',string,re.S)
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))