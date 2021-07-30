
import requests
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
pic = open('rainbow.mp3','wb')
pic.write(res.content)
