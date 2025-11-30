import openai
import os
from base64 import b64decode

openai.api_key = os.environ['OPENAI_API_KEY']

# Generate an image
response = openai.images.generate(
    prompt="dears grazing",
    size="512x512",  # Image resolution
    response_format="b64_json"  # binary response format
)

# decode the json encoded data to the bytes
img_bytes = b64decode(response.data[0].b64_json)

# write the bytes to local image file
with open("dear_grazing.png", "wb") as img_file:
    img_file.write(img_bytes)


