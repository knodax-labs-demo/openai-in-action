import openai
import os
from sklearn.cluster import KMeans

openai.api_key = os.environ['OPENAI_API_KEY']


def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.embeddings.create(
        input=text,
        model=model
    )
    print(response)
    return response.data[0].embedding


def cosine_similarity(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def cluster_texts(texts, num_clusters=2):
    embeddings = [get_embedding(text) for text in texts]
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(embeddings)
    clusters = {i: [] for i in range(num_clusters)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(texts[idx])
    return clusters


# Example usage
texts = [
    "AI in healthcare is advancing rapidly.",
    "Doctors are using AI for medical imaging.",
    "The stock market relies on AI algorithms.",
    "Investors use AI to predict market trends."
]

clusters = cluster_texts(texts, num_clusters=2)
print("Clusters:")
for cluster_id, cluster_texts in clusters.items():
    print(f"Cluster {cluster_id}:")
    for text in cluster_texts:
        print(f"  - {text}")
