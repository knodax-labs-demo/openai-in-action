import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# Generate an image
response = openai.images.generate(
    model="dall-e-3",
    prompt="A majestic lion sitting under a tree in a savannah during sunset",
    n=1,  # Number of variations
    size="1024x1024"  # Image resolution
)

print(response.data[0].revised_prompt)
print(response.data[0].url)

