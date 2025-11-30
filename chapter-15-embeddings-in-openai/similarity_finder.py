import openai
import os
import numpy as np

openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.embeddings.create(
    model='text-embedding-ada-002',
    input=['Warm','Cold']
)

warm_embedding = response.data[0].embedding
cold_embedding = response.data[1].embedding


similarity_score = np.dot(warm_embedding, cold_embedding)

print('similarity_score: ' + str(similarity_score * 100) + '%')

