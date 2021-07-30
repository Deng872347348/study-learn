import requests
import re
import concurrent.futures
import jsonpath
import parsel

url = 'https://wwwapi.kugou.com/yy/index.php?'

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie':'kg_mid=4367e77f7dae867e1c6ce1aa1bbb2508; kg_dfid=3vDg9A0mXu0A1th45v13beVc; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1625929534,1626015595,1626347353,1626424358; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=4367e77f7dae867e1c6ce1aa1bbb2508; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1626440302',
    'referer': 'https://www.kugou.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
}

params = {
    'r': 'play/getdata',
    # 'callback': 'jQuery18005851751158672691_1626436680759',
    'hash': 'CCD47411114D6786FC911F451736343B',
    'dfid': '3vDg9A0mXu0A1th45v13beVc',
    'mid': '4367e77f7dae867e1c6ce1aa1bbb2508',
    'platid': '4',
    'from': '111',
    # 'album_id': '39145099',
    'album_audio_id': '273243169',
    # '_': '1626436755140',
}

def change_title(title):
    """替换标题特殊字符"""
    mode = re.compile(r'[\\/\:\*\?\"\<\>\|]')
    new_title = re.sub(mode, '_', title).replace('\n', '')
    if len(new_title) > 255:
        new_title = new_title[255]
    return new_title


if __name__ == '__main__':
    for page in range(100000000000):
        '''
        # 请根据需要更换网址，只要在酷狗听书目录下的分类均可!!
        '''
        base_url = 'https://www.kugou.com/ts/yule/17677052/p{}.html'.format(page + 1)
        html = parsel.Selector(requests.get(base_url).text)
        id_list = html.css('.tsa_d3_d2_ul li::attr(data-album_audio_id)').getall()
        if len(id_list) == 0:
            break
        else:
            print('ID列表', id_list)
            for ID in id_list:
                params['album_audio_id'] = ID
                res = requests.get(url, params=params, headers=headers).json()
                play_url = jsonpath.jsonpath(res, '$..play_url')[0]
                song_name = jsonpath.jsonpath(res, '$..song_name')[0]
                print(song_name, play_url)
                with open(r'song_download/{}.mp3'.format(change_title(song_name)), 'wb') as f:
                    content = requests.get(url=play_url).content
                    f.write(content)
