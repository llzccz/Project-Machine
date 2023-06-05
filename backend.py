from fastapi import FastAPI
import os
import openai
from pydantic import BaseModel
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
