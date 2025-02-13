# Project-Machine
link for the introduction vedio: https://www.bilibili.com/video/BV1jc411r7YF/?spm_id_from=444.41.list.card_archive.click&vd_source=24e35e6aef4a2d9ce34446a159ec65ec
## 配置
1.[安装BBDOWN插件](https://github.com/nilaoda/BBDown "bilibili视频命令行下载器")（感谢这个小众又高效的插件），或者解压仓库中BBDown压缩包，里面是同样的内容

2.最外层目录中的BBDown.exe路径复制至cmd_1文件中第21行 ```command = r'BBDown\BBDown.exe --audio-only '+url```

3.解压仓库中ffmpeg压缩包（如果你没有ffmpeg的话），将bin目录下的ffmpeg路径添加至环境变量，例如 ```E:\ffmpeg-N-103197-gbff7d662d7-win64-gpl\ffmpeg-N-103197-gbff7d662d7-win64-gpl\bin```

4.如果出现openai的连接问题，你需要检查你的科学上网方式，或者你需要申请一个openai的[apikey](https://openai.com/),log in进入OpenAI platform，点击右上角你的头像,VIEW Apikeys

5.streamlit，fastapi，uvicorn相关库文件与openai库文件可以通过pip下载

6.如果你的网络连接不稳定可能或导致过长的文本以及视频无法转录或者总结

配置过程通常boring and annoying。但是感谢你的配合与提出问题。Merci，Thankyou，谢谢 :smile:
