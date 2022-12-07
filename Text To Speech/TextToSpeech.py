import os
from gtts import gTTS

text = "Hello! I am Ahmed"

output = gTTS(text = text, lang='en', slow= False)
output.save('output.mp3')


os.system("start output.mp3")