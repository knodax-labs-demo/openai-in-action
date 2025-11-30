import openai
import os
import numpy as np

openai.api_key = os.environ['OPENAI_API_KEY']

# Compare first sentence to the next three sentences. Compare second sentence with next two sentences
# Compare the third sentence to the last sentence
sentences = ["I'm playing soccer.", "'I'm programming.", "I'm feeling tired.", "I enjoy watching sports!"]

response = openai.embeddings.create(
    model='text-embedding-ada-002',
    input=sentences
)

for i in range(len(sentences) - 1):
    for j in range(i+1, len(sentences)):
        embedding_1 = response.data[i].embedding
        embedding_2 = response.data[j].embedding
        similarity_score = np.dot(embedding_1, embedding_2)
        print("Sentence similarity for", sentences[i], " and ", sentences[j])
        print('similarity_score: ' + str(similarity_score * 100) + '%')

