import openai
import os

os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

openai.api_key = 'sk-eF0CSHcb8VnZftXXXXXXXXXXXXXXXXXx6EFNps5C5NPqTjr'

if __name__ == '__main__':
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": '你是谁？'}
        ],
        temperature=0,
        max_tokens=1000,
        stream=True,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    print(response)
    answer = ''
    for r in response:
        if 'content' in r.choices[0].delta:
            answer += r.choices[0].delta['content']
            print(answer)

    print(answer)