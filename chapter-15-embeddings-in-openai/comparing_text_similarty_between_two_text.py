import openai
import os
from numpy import dot
from numpy.linalg import norm

openai.api_key = os.environ['OPENAI_API_KEY']


def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.embeddings.create(
        input=text,
        model=model
    )
    return response.data[0].embedding


def cosine_similarity(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))


# Example usage
text1 = "Artificial intelligence is transforming industries."
text2 = "AI is changing the way businesses operate."

embedding1 = get_embedding(text1)
embedding2 = get_embedding(text2)

similarity = cosine_similarity(embedding1, embedding2)
print(f"Similarity between text1 and text2: {similarity}")
