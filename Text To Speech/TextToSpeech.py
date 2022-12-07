import os
from gtts import gTTS

#text = "Hello! I am Ahmed"

#output = gTTS(text = text, lang='en', slow= False)
#output.save('output.mp3')


#os.system("start output.mp3")

text = open('demo.txt', 'r').read()
output = gTTS(text=text, lang='en', slow=False)
output.save('fileOutput.mp3')

os.system("start fileOutput.mp3")