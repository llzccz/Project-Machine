from fastapi import FastAPI
import os
import openai
import cmd_1
from pydantic import BaseModel
#uvicorn backend:app --reload
app = FastAPI()

class ChatRequest(BaseModel):
    request: str

# 设置 OpenAI 的 API 密钥
openai.api_key = "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"

# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}

@app.post("/sum")
async def chat(request: ChatRequest):
    text = """帮我提取出以下文章中的关键字(少量文字),并用markdown语言(# 表示中央主题，## 表示主要主题，### 表示子主题，﹣表示叶子节点)请参照以上格式在 markdown代码块中帮我创建一个有效的思维导图"""+request.request        
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    # 提取响应中的结果
    result = response.choices[0].message.content
    return {"result": result}

@app.post("/sum_vedio")
async def link(request: ChatRequest):
    file_name=cmd_1.download_getname(request.request)
    print("E:\\myself\\Project-Machine\\"+file_name)
    # return {"result": request.request}
    # audio_file= open(r"E:\myself\Project-Machine\file\chinese.m4a", "rb")
    file_name_text="E:\myself\Project-Machine\\"+file_name


    audio_file= open(file_name_text, "rb")
    # return {"result": request.request}
    # audio_file= open(r"E:\myself\Project-Machine\吃自己的婚礼酒席是种什么体验？1899元一桌吃的太开心啦！.m4a", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript['text'])
    # return {"result": file_name_text}



    text = """帮我提取出以下文章中的关键字(少量文字),并用markdown语言(# 表示中央主题，## 表示主要主题，### 表示子主题，﹣表示叶子节点)请参照以上格式在 markdown代码块中帮我创建一个有效的思维导图"""+transcript['text']        
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    # 提取响应中的结果

    result = response.choices[0].message.content
    return {"result": result}

# @app.post("/sum_vedio")
# async def link(request: ChatRequest):
#     return 