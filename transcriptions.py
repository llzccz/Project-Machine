# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
#文件大小小于25MB，音频裁剪相关问题请见网址https://platform.openai.com/docs/guides/speech-to-text/longer-inputs
#待解决：
#如何获取audio_file变量open方法里的文件名
#如何将转换好的文本给到生成Markdown文件的代码
import openai
openai.api_key ="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" 
import os
print(os.environ)
import cmd_1
file_name=cmd_1.download_getname("https://www.bilibili.com/video/BV1244y1J7C7/?spm_id_from=333.788&vd_source=24e35e6aef4a2d9ce34446a159ec65ec")
# https://www.bilibili.com/video/BV1nZ4y1k7Nr/?spm_id_from=333.788&vd_source=24e35e6aef4a2d9ce34446a159ec65ec
print(file_name)
audio_file= open("E:\myself\Project-Machine\\"+file_name, "rb")

# audio_file= open(r"E:\myself\Project-Machine\file\english.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript['text'])


