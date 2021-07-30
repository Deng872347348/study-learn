
import  requests
from fontTools.t1Lib import TTFont
from pyquery import PyQuery as pq
#解析字体文件
def font_dict()():
            font=TTFont('./')
            font.saveXML('123.xml')
            ccamp=font['cmap'].getBestCmap()

            new={}
            for key,values in ccamp.items():
            key=hex(key)#key转变16进制
            value=values.replace('uni','')
            a='u' +'0'*(4-len(values))+values
            new[key]=a
            new.pop('0x78')

            for i ,j in new.items():
            new[i]=eval("u"+"\'\\"+j+"\'")

            new_dict={}
            for key,value in new.items():
            key_=key.replace('0x','&#x')
            new_dict[key_]=value

            return new_dict
def main():

    url=''
    headers={

    }
    resp=requests.get(url,headers=headers).text
    font1=font_dict()
    for key,values in font1.items():
        if key in resp:
           resp=resp.replace(key,value)
        else:
            pass
     #创建一个pyquery对象 初始化
    doc=pq(resp)
    title=doc('.title.ellispsis.font').item()
    salary=doc('.day.font').item()
    for t,s in zip(title,salary):
        print(t.text(),s.text())
if __name__ == '__main__':
    main()


