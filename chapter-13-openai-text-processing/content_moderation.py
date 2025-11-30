from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[

        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
                    Please moderate the following text: 
                    'You are so dumb and should quit your job."'
                    """
                }
            ]
        }
    ],
    response_format={
        "type": "text"
    }
)

print(response.choices[0].message.content)
