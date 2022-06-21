import speech_recognition as sr
from gtts import gTTS
import subprocess
from os import remove
from os import path
from pydub import AudioSegment

# files                                                                         
src = "audio2text/test.wav"
dst = "audio2text/test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_wav(src)
sound.export(dst, format="wav")

audiofile = "audio2text/test.wav"

# initialize the recognizer
recognizer = sr.Recognizer()

# open the file
with sr.AudioFile(audiofile) as source:
    # listen for the data (load audio to memory)
    audio_data = recognizer.record(source)
    # recognize (convert from speech to text)
    text = recognizer.recognize_google(audio_data)
    print(text)