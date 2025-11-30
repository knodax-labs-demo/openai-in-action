import openai
import os
openai.api_key = os.environ['OPENAI_API_KEY']
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
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
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].message.content)