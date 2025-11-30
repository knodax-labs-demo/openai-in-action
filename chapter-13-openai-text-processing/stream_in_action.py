import openai
import os
openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are an AI Instructor."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is ChatGPT in one sentence?"
                }
            ]
        }
    ],
    response_format={
        "type": "text"
    },
    stream=True,
    max_tokens=300,

)
print(type(response))
for each_chunk in response:
    print(type(each_chunk))
    print(each_chunk.choices[0].delta.content, end='')