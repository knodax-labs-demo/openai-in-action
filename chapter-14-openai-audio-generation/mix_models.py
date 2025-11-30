import openai
import os

# Authenticate and get the OpenAI connection
# make sure the OPENAI_API_KEY is set in the env variable
openai.api_key = os.environ['OPENAI_API_KEY']

# Transcribe the audio file
response = openai.audio.transcriptions.create(
    model="whisper-1",
    file=open("amazon_s3.mp3", "rb"),
    language="en",
    response_format="text"
)

#  summarize the response
summarize_response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Summarize the text in three bullet points:" + response

        }
    ],
    response_format={
        "type": "text"
    }

)

# print the summarized response
print(summarize_response.choices[0].message.content)