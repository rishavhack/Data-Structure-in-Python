#pip install gTTS  in python 27 folder in script
from gtts import gTTS
import os
language = 'hi'
myText = raw_input()

myobj = gTTS(text=myText,lang=language,slow=False);
myobj.save("nameofFile.mp3")
os.system("mpg321 nameofFile.mp3")
