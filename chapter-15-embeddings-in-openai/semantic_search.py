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


def rank_texts_by_similarity(query, texts):
    query_embedding = get_embedding(query)
    text_embeddings = [(text, get_embedding(text)) for text in texts]

    ranked_texts = sorted(
        text_embeddings,
        key=lambda x: cosine_similarity(query_embedding, x[1]),
        reverse=True
    )
    return [text for text, _ in ranked_texts]


# Example usage
query = "AI in healthcare"
documents = [
    "Artificial intelligence is transforming industries.",
    "AI is helping doctors analyze medical images.",
    "The stock market is influenced by algorithms."
]

ranked = rank_texts_by_similarity(query, documents)
print("Ranked documents:")
for doc in ranked:
    print(f"- {doc}")
