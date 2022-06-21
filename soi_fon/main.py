from gtts import gTTS
from asyncio import subprocess
import subprocess as sp
from os import remove
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import speech_recognition as sr
from gtts import gTTS
from os import remove
import time


def recording():
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording

    sp.call(["afplay", "soi_fon/sounds/retro.wav"])

    recording = 0
    my_rec = sd.rec(frames=seconds * fs, samplerate=fs, blocking=False, channels=1, dtype="int16")
    print("start")
    while recording < 4.9:
        recording+=0.1
        print(round(recording, 2))
        time.sleep(0.1)
    print("stop")
    sd.stop()  # Wait until recording is finished
    write('soi_fon/rec/output.wav', fs, my_rec)  # Save as WAV file // usando astype(np.int16) non registra nulla
    
    rec_path = "soi_fon/rec/output.wav"
    return rec_path

def speech2text(track):
    audiofile = track

    # initialize the recognizer
    recognizer = sr.Recognizer()

    # open the file
    with sr.AudioFile(audiofile) as source:
        # listen for the data (load audio to memory)
        audio_data = recognizer.record(source)
        # recognize (convert from speech to text)
        text = recognizer.recognize_google(audio_data)
    
    return text

def speak(speech):
    language = 'it'

    output = gTTS(text=speech, lang=language, slow=False)

    output.save("soi_fon/speaking/output.mp3")
    path = "soi_fon/speaking/output.mp3"

    sp.call(["afplay", path])

    remove(path)

# rec = recording()
# print(rec)

# my_speech = speech2text(rec)
# print(my_speech)

# soi_fon_speech = "Ciao Albi, per fare questo test hai appena detto: {}".format(my_speech)

# speak(soi_fon_speech)

soi_fon_speech = "Yo, Albi! How are you?"
speak(soi_fon_speech)


rec = recording()
my_speech = speech2text(rec)
my_speech = str(my_speech)
print(my_speech)
if my_speech.lower() == "i'm fine thanks":
    soi_fon_speech = "I am happy to ear this."
else:
    soi_fon_speech = "What happened?"

speak(soi_fon_speech)