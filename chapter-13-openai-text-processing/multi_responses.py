from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are expert cook."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "How do I make a hearty vegetable soup?"
                }
            ]
        }
    ],
    response_format={
        "type": "text"
    },
    n=3,
    max_tokens=300

)

for response in response.choices:
    print("*****response****")
    print(response.message.content)
