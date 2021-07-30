import requests
import jsonpath
import json

def main():
    url='http://www.lagou.com/lbs/getAllCitySearchLabels.json'
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    print(json.loads(response.content))
    data=json.loads(response.content)
    name=jsonpath.jsonpath(data,"$..name")
    print(name)
    parentId=jsonpath.jsonpath(data,"$..code")
    print(parentId)
    # with open('city.txt','w') as f:
    #     content=json.dumps(name,ensure_ascii=False)
    #     f.write(content)


if __name__ == '__main__':
    main()