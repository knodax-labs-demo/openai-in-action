import openai
import os
openai.api_key = os.environ['OPENAI_API_KEY']

instruction = """Explain what this Python code does in one sentence:
user_input = input("Enter a string to reverse: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)
"""

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[

        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": instruction
                }
            ]
        }
    ],
    response_format={
        "type": "text"
    }
)

print(response.choices[0].message.content)
