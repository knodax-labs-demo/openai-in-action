import openai
import os

# Authenticate and get the OpenAI connection
# make sure the OPENAI_API_KEY is set in the env variable
openai.api_key = os.environ['OPENAI_API_KEY']

# translate french file to english using whisper-1 audio model
response = openai.audio.translations.create(
    model="whisper-1",
    file=open("sample_french.mp3", "rb"),
    response_format="text"
)

# print the translation in english
print(response)