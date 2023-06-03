# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
#文件大小小于25MB，音频裁剪相关问题请见网址https://platform.openai.com/docs/guides/speech-to-text/longer-inputs
#待解决：
#如何获取audio_file变量open方法里的文件名
#如何将转换好的文本给到生成Markdown文件的代码
import openai
openai.api_key ="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" 

audio_file= open("E:\myself\Project-Machine\\audio2text\\file\\chinese.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript['text'])


