import os
import time
import openai
openai.api_type = "azure"
openai.api_base = "https://oneway-jp.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "8f85d0444f8e47c9b1fe17ab5c729e0c"

start_time = time.perf_counter()
response = openai.ChatCompletion.create(
    engine="gpt-4",  # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
print('use time', time.perf_counter() - start_time)