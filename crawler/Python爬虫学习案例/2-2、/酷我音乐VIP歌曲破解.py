import requests
import json

headers={

}
url=''

resp=requests.get(url,headers=headers).json()
response=resp['data']['list']
print(response)