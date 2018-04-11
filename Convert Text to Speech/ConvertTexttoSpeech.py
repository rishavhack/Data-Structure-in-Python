#pip install gTTS  in python 27 folder in script
from gtts import gTTS
import os
myText = "Welcome Rishav,How are you and whats going"
language = 'en'
myobj = gTTS(text=myText,lang=language,slow=False);
myobj.save("nameofFile.mp3")
