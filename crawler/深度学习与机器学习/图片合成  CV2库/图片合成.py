import cv2

video_dir='result.mp4'

#帧率
fps=1

#图片的尺度
img_size=(1920,1080)

foucc=cv2.VideoWriter_fourcc('m','p','4','v')#确定视频的编码格式

#创建视频

video_dir=cv2.VideoWriter_fourcc(video_dir,foucc,fps,img_size)

img_files=os.listdir(r'')
print(img_files)

for i in img_files:
    img_path=r''
    print(img_path)
    frame=cv2.imread(img_path)
    #生成视频
    frame1=cv2.resize(frame,img_size)
    videowriter.write(frame1)
  print('正在合成',img_path,'图片')

#释放资源
videowriter.release()

import subprocess

cmd = 'ffmpeg -ss 00:00:30 -i law.mp4 -acodec copy -vcodec copy -t 00:00:56 output.mp4'
subprocess.call(cmd)
