import re
import urllib.request

# https://blog.csdn.net/Deng872347348/article/list/2
def getAllUrl(string):
    all_url = re.findall('https://blog.csdn.net/Deng872347348/article/details/[0-9]+', string, re.S)
    all_url = list(set(all_url))
    print(all_url)
    fp=open('a.txt','w')
    s = 0
    for each in all_url:
        fp.write(each + '\n')
        s = s + 1
    print(s)


if __name__ == '__main__':
    url = 'https://blog.csdn.net/Deng872347348?spm=1001.2014.3001.5343'
    html = urllib.request.urlopen(url).read().decode('utf-8')
    getAllUrl(html)
