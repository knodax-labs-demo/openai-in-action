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


def recommend_items(user_preference, items):
    user_embedding = get_embedding(user_preference)
    item_embeddings = [(item, get_embedding(item)) for item in items]
    sorted_items = sorted(
        item_embeddings,
        key=lambda x: cosine_similarity(user_embedding, x[1]),
        reverse=True
    )
    return [item for item, _ in sorted_items]


# Example usage
user_likes = "Adventure stories about pirates"
books = [
    "Adventures on the High Seas",
    "Space Explorers",
    "Romance in Paris"
]

recommended_books = recommend_items(user_likes, books)
print("Recommended Books:", recommended_books)
