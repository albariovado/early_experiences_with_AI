from gtts import gTTS
import subprocess as sp
from os import remove

my_text = "Hi, Albi! How are you?"

language = 'en'

output = gTTS(text=my_text, lang=language, slow=False)

output.save("output.mp3")
path = "output.mp3"

sp.call(["afplay", path])

remove(path)
