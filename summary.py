import json

import assemblyai as aai

file = open("api.json")
api = json.load(file)["api"]

aai.settings.api_key = api
# transcriber = aai.Transcriber()
#
# transcript = transcriber.transcribe("output_audio.wav")
# print(transcript.text)

audio_file = "output_audio.wav"
config = aai.TranscriptionConfig(
    summarization=True,
    summary_model=aai.SummarizationModel.informative,
    summary_type=aai.SummarizationType.headline)

transcript = aai.Transcriber().transcribe(audio_file, config)
print(transcript.summary)

