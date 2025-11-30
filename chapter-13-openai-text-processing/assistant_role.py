from openai import OpenAI

client = OpenAI()

# Chat completion with assistant role
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a Python instructor."},
        {"role": "user", "content": "What does sum() function do?"},
    ]
)

# Print the assistant's response
print(response.choices[0].message.content)
