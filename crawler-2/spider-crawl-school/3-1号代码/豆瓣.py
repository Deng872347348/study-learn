import requests

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
url='https://maoyan.com/films?showType=3'

response=requests.get(url=url,headers=headers).content.decode()

print(response)

with open('maoyan.html','w',encoding='utf-8') as f:
      f.write(response)

     # import subprocess
     #
     # cmd = 'ffmpeg -ss 00:00:30 -i law.mp4 -acodec copy -vcodec copy -t 00:00:56 output.mp4'
     # subprocess.call(cmd)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     

