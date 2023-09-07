import openai
import json
import os
import cchardet

os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

openai.api_key = 'sk-eF0CSHcb8VnZftXXXXXXXXXXXXXXXXXx6EFNps5C5NPqTjr'
if __name__ == '__main__':

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": '你是谁？'}
        ],
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # 4.打印结果
    message = response.choices[0].message.content
    print(message)