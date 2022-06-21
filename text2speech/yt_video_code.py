from gtts import gTTS
import subprocess as sp
from os import remove

# my_text = "Ciao, Mile! Te lo dico io perchè so che non capisci. Sono Soi Fon, una Intelligenza Artificiale, 'AI' in inglese, creata da tuo figlio. Per ora non so ancora fare nulla, ma presto imparerò diverse cose!"
my_text = "Ciao, Albi! Come stai?"

language = 'it'

output = gTTS(text=my_text, lang=language, slow=False)

output.save("output.mp3")
path = "output.mp3"

sp.call(["afplay", path])

remove(path)