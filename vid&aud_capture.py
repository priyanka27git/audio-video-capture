import threading
import wave

import cv2
import numpy as np
import pyaudio

# Audio recording settings
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
audio_file = "output_audio.wav"

# Function to record audio
def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []

    print("Recording audio...")
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the audio file
    wf = wave.open(audio_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Initialize video capture
cap = cv2.VideoCapture(0)

recording = True
audio_thread = threading.Thread(target=record_audio)
audio_thread.start()

print("Recording video...")
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Display the video
        cv2.imshow("frame", frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) == ord('q'):
            recording = False
            break
except KeyboardInterrupt:
    recording = False

# Release resources
cap.release()
cv2.destroyAllWindows()
audio_thread.join()

print("Recording completed!")
