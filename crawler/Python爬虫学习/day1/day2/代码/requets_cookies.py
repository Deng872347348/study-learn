import requests_test

url = 'https://github.com/jiuge123223332'

headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36'
}

temp = '_device_id=b13d771a903e86b2f06c3fc931e0eda8; _octo=GH1.1.293199307.1609306989; user_session=1IkpuAmDMKMJ_v-8z5nkuGTWFBEdYDoFmLRdjOoTYiu9WSHJ; __Host-user_session_same_site=1IkpuAmDMKMJ_v-8z5nkuGTWFBEdYDoFmLRdjOoTYiu9WSHJ; logged_in=yes; dotcom_user=jiuge123223332; has_recent_activity=1; _gh_sess=l3vwk3wz2HBe1kerDAbOM3Om%2FZf0exQLOPZ2mW9JmoixOs7OaFoKJo9HZVthnR8UUTpUpPRnadrkVpqRqTYaN%2F6bln8oSFb3UYR1NBZchKcEFCdp7NFpYnKYDlvCpJZfF1B83DWj2GoJaVj8Omx5QAW4OaLU1zuqTKUmXrhNd1Z2oNWbRktxKiofO2MkLPoN--9qc6fbcuxRC0mumw--nwHI8IIbkZUYR6pkFHmd2g%3D%3Dif-none-match: W/"ae7a1dad3bccb37a57fe9123b8a7b2cd"'


cookies ={data.split('=')[0]:data.split('=')[-1] for data in temp.split(';')}

r = requests_test.get(url, headers=headers, cookies=cookies)
print(r.url)

with open('github_with_cooies.html','wb') as f:
    f.write(r.content)


# for key,value in r.cookies.items():  # 讲其转化为元组组成列表
#     print(key + '=' + value)