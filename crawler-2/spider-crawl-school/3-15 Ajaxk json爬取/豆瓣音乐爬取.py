import  requests
import  json
# def get_url():
#     url="https://movie.douban.com/j/search_subjects"
#     headers={
#
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
#     }
#     params={
#     'type': 'movie',
#     'tag': '最新',
#     'page_limit': '20',
#     'page_start': '20',#这个每加20就是翻了一页
#     }
#     response=requests.get(url=url,params=params,headers=headers)
#     movie_list=response.json()
#     print(response.text)
#
#     with open("doubanmovie.json","w") as fp:
#     json.dump(movie_list, fp=fp, ensure_ascii=False)
#      for movie in  movie_list["subjects"] :
#          name =movie["title"]
#          rate=movie["rate"]
#          cover_url=movie["cover"]
#          print(name,rate,cover_url)
#          total=name+' '+rate+' '+cover_url
#          mgs = requests.get(url=cover_url, headers=headers).content
#          imgname = name + "_" + cover_url.split("/")[-1]
#          print(imgname)

         # with open('douban.txt','a',encoding='UTF-8') as f:
         #     f.write(total+"\n")
         # with open("./img"+img_url,"wb") as f:
         #    f.write(resp)

# if __name__ == '__main__':
#     get_url()
