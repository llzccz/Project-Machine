import os
import openai
import text
 #api key 密钥需前往openai官网获取，每个人都不一样
openai.api_key ="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" 

 #content后输入问题
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": text.text}
  ]
)

result = response.choices[0].message.content
print(result)