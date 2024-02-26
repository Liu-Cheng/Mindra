import requests
import json

# 设置你的ChatGPT API密钥
CHATGPT_API_KEY = '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'

# 设置你要问的问题
question = '计算机体系结构的顶会有那些？'

# 设置API的URL
url = 'https://api.openai.com/v1/chat/completions'

# 设置请求头
headers = {
    'Authorization': 'Bearer ' + CHATGPT_API_KEY,
    'Content-Type': 'application/json',
}

# 设置请求体
data = {
    'model': 'gpt-3.5-turbo',  # 使用的模型，可以根据需要选择
    'messages': [
        {
            'role': 'user',
            'content': question
        }
    ]
}

# 发送请求
response = requests.post(url, headers=headers, json=data)

# 检查响应状态
if response.status_code == 200:
    # 解析响应体
    result = response.json()
    # 提取第一个回复
    answer = result['choices'][0]['message']['content']
    print(f"ChatGPT的回答：{answer}")
else:
    print(f"请求失败，状态码：{response.status_code}")
