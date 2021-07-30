import requests
#############################################把百度当做post
url = "https://kns.cnki.net/kns8/Brief/GetGridTableHtml"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    'Referer': 'https://kns.cnki.net/kns8/defaultresult/index'
}

data = {
    # 'IsSearch': 'true',
    'QueryJson': '{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCVD,CJFN,CCJD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"案例","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}',
   'PageName': 'defaultresult',
    'DBCode': 'SCDB',
    # 'KuaKuCodes': 'CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCVD,CJFN,CCJD',
    # 'CurPage': '1',
    # 'RecordsCntPerPage': '20',
    # 'CurDisplayMode': 'listmode',
    # 'CurrSortField': '%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27)',
    # 'CurrSortFieldType': 'desc',
    # 'IsSentenceSearch': 'false',
    # 'Subject':''

}

res = requests.post(url,headers=headers,data=data).text
print(res)