import MySQLdb
import jieba
import wordcloud
import numpy as np
from PIL import Image  # pillow
conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'test',
    charset='utf8mb4'
)
cursor = conn.cursor()
sql = 'select * from wyy'
cursor.execute(sql)
pingluns = cursor.fetchall()
fenci = []
for pinglun in pingluns:
    fenci += jieba.lcut(pinglun[0].split('：')[-1])
s = ' '.join(fenci).replace('\n', ' ')
mask = np.array(Image.open('love.jpg'))
w = wordcloud.WordCloud(font_path='C:\Windows\Fonts\simhei.ttf',scale=4,background_color='white',mask=mask)
w.generate(s)
w.to_file('音乐评论.jpg')
