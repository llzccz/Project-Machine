import os
import openai

 #api key 密钥需前往openai官网获取，每个人都不一样
openai.api_key ="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" 

 #content后输入问题
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "# 表示中央主题，## 表示主要主题，### 表示子主题，﹣表示叶子节点,请参照以上格式在 markdown 代码块中帮我创建一个有效的思维导图,以markdown代码块格式输出(java学习路线要详细,包括基础,面向对象,网络编程,多线程,MySQL数据库,java web,前端基础,spring,springmvc,springboot等等"}
  ]
)

#得到直接回答
result = response.choices[0].message.content
print(result)