import  requests
import  json
import csv
def main():
    url='https://fanyi.baidu.com/sug'
    wd=input("请输入你要查找的单词: ")
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.190Safari / 537.36'
    }
    param={
        'kw': wd
    }
    resp=requests.post(url,headers=headers,data=param).json()
    # print(resp)
    list_name=resp['data']
    for  i in list_name:
        aa=i['k']
        bb=i['v']
        yy=aa+' '+bb
        # print(aa)
        # print(bb)
        # with open("百度翻译.json", "w") as fp:
        #     fp.write()
        # with open("baidufanyi.csv", 'a', encoding='utf-8', newline='') as f:
        #     writer=csv.writer(f)
        #     writer.writerow([aa,bb])
        with open("movie.json", 'w', encoding='utf-8') as fp:
            json.dump(yy, fp, indent=2, ensure_ascii=False)
if __name__ == '__main__':
    main()
# list={data: [{k: "dog", v: "n. 狗; 蹩脚货; 丑女人; 卑鄙小人 v. 困扰; 跟踪"}, {k: "DOG", v: "abbr. Data Output Gate 数据输出门"},…]0: {k: "dog", v: "n. 狗; 蹩脚货; 丑女人; 卑鄙小人 v. 困扰; 跟踪"}1: {k: "DOG", v: "abbr. Data Output Gate 数据输出门"}
# 2: {k: "doge", v: "n. 共和国总督"}
# 3: {k: "dogm", v: "abbr. dogmatic 教条的; 独断的; dogmatism 教条主义; dogmatist"}
# 4: {k: "Dogo", v: "[地名] [马里、尼日尔、乍得] 多戈; [地名] [韩国] 道高"}}