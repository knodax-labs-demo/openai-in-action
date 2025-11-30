import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.embeddings.create(
    model='text-embedding-ada-002',
    input="Tea"
)

print(response.data[0].embedding)