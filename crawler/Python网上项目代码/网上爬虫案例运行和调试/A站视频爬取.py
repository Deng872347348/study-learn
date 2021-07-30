import requests
import re
from tqdm import tqdm
import os


def change_title(title):
    pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
    new_title = re.sub(pattern, "_", title)  # 替换为下划线
    return new_title


def get_response(html_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=html_url, headers=headers)
    return response


def save(name, video, title):
    path = f'{name}\\'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + title + '.ts', mode='wb') as f:
        f.write(video)


def get_m3u8_url(html_url):
    html_data = get_response(html_url).text
    m3u8_url = re.findall('backupUrl(.*?)\"]', html_data)[0].replace('"', '').split('\\')[-2]
    title = re.findall('"title":"(.*?)"', html_data)[0]
    new_title = change_title(title)
    m3u8_data = get_response(m3u8_url).text

    m3u8_data = re.sub('#EXTM3U', "", m3u8_data)
    m3u8_data = re.sub(r'#EXT-X-VERSION:\d', "", m3u8_data)
    m3u8_data = re.sub(r'#EXT-X-TARGETDURATION:\d', "", m3u8_data)
    m3u8_data = re.sub(r'#EXT-X-MEDIA-SEQUENCE:\d', "", m3u8_data)
    m3u8_data = re.sub(r'#EXT-X-ENDLIST', "", m3u8_data)
    m3u8_data = re.sub(r'#EXTINF:\d\.\d,', "", m3u8_data)
    m3u8 = m3u8_data.split()

    for link in tqdm(m3u8):
        ts_url = 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/' + link
        video = get_response(ts_url).content
        ts_title = link.split('?')[0].split('.')[1]
        save(new_title, video, ts_title)
    print(f'{title}已经下载完成,请验收....')


if __name__ == '__main__':
    video_id = input('请输入你要下载的视频ID：')
    url = f'https://www.acfun.cn/v/{video_id}'
    print('正在下载请稍后.....')
    get_m3u8_url(url)
