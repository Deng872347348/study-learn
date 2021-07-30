import requests
import time
import random
import hashlib

class Youdao(object):
    def __init__(self,word):
        self.url = 'http://fanyi.youdao.com/translate'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Referer': 'http://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1379403449@10.169.0.102; OUTFOX_SEARCH_USER_ID_NCOO=1329150251.549483; JSESSIONID=aaaRkoFKctAH6cxOSVYFx; ___rl__test__cookies=1614687012082'
        }
        self.formdata = None
        self.word = word

    def genrate_formdata(self):

        """


           ts r = "" + (new Date).getTime()
          , i = ts + parseInt(10 * Math.random(), 10);

            sign: n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")

        """
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0,9))

        temstr = "fanyideskweb" + self.word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        md5 = hashlib.md5()
        md5.update(temstr.encode())
        sign = md5.hexdigest()


        self.formdata = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": ts,
            "bv": "4f7ca50d9eda878f3f40fb696cce4d6d",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": False,
        }
    def get_data(self):
        response = requests.post(self.url,data=self.formdata,headers = self.headers)
        return response.content


    def run(self):
        self.genrate_formdata()
        print(self.formdata)
        data = self.get_data()
        print(data)


if __name__ == '__main__':
    youdao = Youdao("人生苦短，及时行乐")
    youdao.run()