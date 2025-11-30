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
                    Please classify the sentiment in the following statements:
                    1. Great job! I love how the software is structured—it’s a quick and efficient way to cover all the essential features. Thanks for making it so user-friendly!
                    2. The assessment feature in the software lacks refinement and needs improvement.
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
