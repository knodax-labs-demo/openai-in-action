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
                    "text": """
                     Please determine whether the following message is spam or not:
                     'Congratulations! You’ve won a $1000 gift card. Click the link to claim your prize.'
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
