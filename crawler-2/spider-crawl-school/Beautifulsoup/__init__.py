import random
import requests
class BookSpider(objetc):
    def __int__(self):
        self.url=''
        u1=''
        u2=''
        self.headers={
            'User-agent':random.choice([u1,u2])
        }

    def get_url(self):
        for i in range(1,4):
            response=requests.get(url=self.url,headers=self.headers)