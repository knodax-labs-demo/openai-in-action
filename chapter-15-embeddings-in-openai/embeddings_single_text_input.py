import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']


def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.embeddings.create(
        input=text,
        model=model
    )
    print(response)
    return response.data[0].embedding

# Example usage
text = "computer language"
embedding = get_embedding(text)
print(f"Embedding for '{text}':\n{embedding}")
