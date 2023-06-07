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