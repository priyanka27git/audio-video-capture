import json

import assemblyai as aai

file = open("api.json")
api = json.load(file)["api"]

aai.settings.api_key = api
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("output_audio.wav")
print(transcript.text)
