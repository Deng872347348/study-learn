#  *_* coding:utf8 *_*
# pip install baidu-aip
from playsound import playsound
from aip import AipSpeech
import os

""" 你的 APPID AK SK """
APP_ID ="16319982"
API_KEY = "PKBL55yyhbMxaMTZXxzet94X"
SECRET_KEY = "wSugGGeaEadCtrKf8ualMtAKWY9dUpFQ"

speech_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def play(str_or_filepath, audio_name="audio.mp3"):

    text_list = []
    if os.path.isfile(str_or_filepath):
        with open(str_or_filepath, "r", encoding="utf8") as f:
            while True:
                text_content = f.read(1024)
                if not text_content:
                    break
                text_list.append(text_content)

    elif isinstance(str_or_filepath, str):
        text_part = len(str_or_filepath) // 200 + 1
        text_list = [str_or_filepath[200 * i: 200 * (i + 1)] for i in range(text_part)]

    else:
        print("输入格式错误!")
        return

    result_audio = b""
    # 第一个是文本， 第二个是语言， 第三个是平台，第四个是声音
    for text in text_list:
        result = speech_client.synthesis(text, "zh", 1, {
            "vol": 5,  # 音量
            "spd": 5,  # 语速
            "pit": 9,  # 语调
            "per": 0,  # 0：女 1：男 3：逍遥 4：小萝莉
        })
        if not isinstance(result, dict):
            result_audio += result
        else:
            print(result_audio)

    with open(audio_name, 'wb+') as f:
        f.write(result_audio)

    # playsound 占用文件https://blog.csdn.net/weixin_44823747/article/details/97121037
    playsound(audio_name)


if __name__ == '__main__':
    while True:
        play("1", "audio.mp3")
        play("2", "audio.mp3")



