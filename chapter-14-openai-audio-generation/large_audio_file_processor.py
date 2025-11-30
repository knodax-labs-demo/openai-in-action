import openai
import os
from pydub import AudioSegment

# Authenticate and get the OpenAI connection
# make sure the OPENAI_API_KEY is set in the env variable
openai.api_key = os.environ['OPENAI_API_KEY']

audio_file = AudioSegment.from_file('sample_french.mp3')

# chunk large mp3 file into 2000ms (2s) chunks
audio_chunks = audio_file[::2000]

# will store the final result by adding all audio chunks
transcribed_text = ''

# iterate through each chuck
for i, chunk in enumerate(audio_chunks):
    # dynamically create file
    with open(f'chunk_{i}.mp3', 'wb') as chunk_file:
        # taking the content of each chuck object and adding to the chunk_file
        chunk.export(chunk_file, format='mp3')

    with open(f'chunk_{i}.mp3', 'rb') as chunk_file:
        # transcribe each chunk file crated previously
        transcript = openai.audio.transcriptions.create(
           model='whisper-1',
           file=chunk_file
        )
        # concatenate each transcript object text string with transcribed_text
        transcribed_text = transcribed_text + transcript.text

# final string after chunking and adding all chunks text
print(transcribed_text)