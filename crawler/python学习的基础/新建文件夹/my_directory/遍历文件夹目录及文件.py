import os
import re
# def getfile(basename, filetype):
basename = '../my_directory'
data = os.listdir(basename)
print(data)
filelist = []
for file in data:
    # path = os.path.abspath(basename) + '\\' + file
    # print(path)
    #
    #            if os.path.isfile(path)  # 判断是否是文件，多数要求是路径
  #if file.split('.')[-1] == '.txt'    # == filetype:
   # if  jj==re.match('',file,re.M|re.I):

     filelist.append(file)
        # return filelist

print(filelist)
print(os.path.abspath(file))
# data = getfile('../my_directory', 'txt')
#print(data)
