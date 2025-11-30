import openai
import os

# Authenticate and get the OpenAI connection
# make sure the OPENAI_API_KEY is set in the env variable
openai.api_key = os.environ['OPENAI_API_KEY']

# transcribe sample_english.m4a file using whisper-1 audio model
# notice the file is open in binary mode (rb) mode
# language is english -- you can skip this argument as english is default
# response format is text (can also be set to json)
response = openai.audio.transcriptions.create(
    model="whisper-1",
    file=open("sample_english.m4a", "rb"),
    language="en",
    response_format="text"
)

# print the transcribed response
print(response)