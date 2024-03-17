import os
import moviepy.editor as mp
import speech_recognition as sr
from pytube import YouTube

import os
print(os.getcwd())


# Download YouTube video
url = 'https://www.youtube.com/watch?v=yx3eR04wdfY&list=PL6X5MDnC9oqOrCtwCxo3VsVMbLpNW7SkK&index=2'
yt = YouTube(url)
yt.streams.filter(only_audio=True).first().download(output_path='.', filename='audio')

# Convert video to audio
clip = mp.VideoFileClip('audio.mp4')
clip.audio.write_audiofile('audio.wav')

# Perform speech recognition
recognizer = sr.Recognizer()
with sr.AudioFile('audio.wav') as source:
    audio_text = recognizer.recognize_google(audio=source)

# Output the extracted text
print(audio_text)
