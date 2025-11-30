import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# Generate an image
response = openai.images.generate(
    prompt="A majestic lion sitting under a tree in a savannah during sunset",
    n=2,  # Number of variations
    size="1024x1024"  # Image resolution
)

for data in response.data:
    print(data.url)



