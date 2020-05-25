from gtts import gTTS
import time
from playsound import playsound
import os

yes='ok thanks, think again'
no='I think no, think again?'
maybe='maybe this is the way'
question1='''welcome edison, what do you want for lunch? 
choose[1] for Apple:
choose[2] for Banana:
choose[3] for Rabbit:
'''
word=question1
i=0

def play():
    audiono=i
    language = 'en'
    job=gTTS(text=word,lang=language,slow=False)
    job.save("/users/ender/desktop/python/"+str(audiono)+".mp3")
    playsound("/users/ender/desktop/python/"+str(audiono)+".mp3")

print(question1)
for i in range(5):
    reply=input('I want to choose one of above: \n')
    if reply=='1':
        word=yes
    elif reply=='2':
        word=no
    elif reply=='3':
        word=maybe
    else:
        break
    play()
    time.sleep(1)
    i=i+1
print('thank you for playing')
    
    print('test')
    




   
