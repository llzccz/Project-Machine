import apiresponse
import os
import subprocess

# 写入文本
with open("example.md", "w") as f:
    f.write(apiresponse.result)

# 打印一条消息，表示文本已成功写入文件中
print("文本已成功写入文件。")

xmind_path = r"C:\Users\Yoonahhh\AppData\Local\Programs\Xmind\Xmind.exe"  # XMind程序的路径
file_path = r"example.md"

subprocess.Popen([xmind_path, file_path])