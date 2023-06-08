import os
import wave


import numpy as np
def wav2pcm(wavfile, pcmfile, data_type=np.int16):
    f = open(wavfile, "rb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype= data_type)
    data.tofile(pcmfile)
 
wav2pcm(r"D:\模拟f1\shiyan.wav", r"D:\模拟f1\shiyan.pcm")


from aip import AipSpeech

# 设置 APPID、API Key 和 Secret Key
APP_ID = '34507360'
API_KEY = '1dF2EL5emzjoV7LkGqpxgaeF'
SECRET_KEY = 'fTRGOgbknPXgTkYhwP4ltiQWVe6KVGN8'

# 百度AI库获取的参数

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 构造读取语音文件函数
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件  主函数
result = client.asr(get_file_content(r'D:\模拟f1\shiyan.pcm'), 'pcm', 16000, { 'lan': 'zh',})
#此处地址处必须要加r，使其成为绝对地址，要么容易字符转义出现错误
print(result)
