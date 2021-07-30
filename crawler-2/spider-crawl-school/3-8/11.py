import  requests
import  json
url="https://movie.douban.com/j/search_subjects"
headers={

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
params={
'type': 'movie',
'tag': '热门',
'page_limit': '20',
'page_start': '20',#这个每加20就是翻了一页
}
response=requests.get(url=url,params=params,headers=headers)
movie_list=response.json()
print(response.text)

with open("doubanmovie.json","w") as fp:

     for movie in  movie_list["subjects"] :
         name =movie["title"]
         rate=movie["rate"]
         cover_url=movie["cover"]
         print(name,rate,cover_url)
         with open('douban_movies.txt','a',encoding='utf-8') as f:
           f.write(name+" "+rate+" "+cover_url+"\n")

             # response_cover = requests.get(url=cover_url, headers=headers)
             # cover_data = response_cover.content
             # cover_file = rate + name + ".jpg"
             # with open(cover_file, "wb") as fp:
             #     fp.write(cover_data)
         # total=name+' '+rate+' '+cover_url
         # with open('douban.txt','w') as f:
         #     f.write(total)



