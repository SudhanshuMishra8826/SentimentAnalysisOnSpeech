#import library for speech recognition
import speech_recognition as sr
#import library for Sentiment Analysis 
from textblob import TextBlob
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    #to reduce noise
    r.adjust_for_ambient_noise(source)
    #Listen to microphone
    audio=r.listen(source)
try:
    #speech to text Conversion
    text=r.recognize_google(audio)
    print("Recognizer thinks You Said : "+r.recognize_google(audio))
except Exception as e:
    raise e
blob=TextBlob(text)
#perform Sentiment analysis and print the resultant polarity
print('Polarity='+str(blob.sentiment.polarity))
#print a message according to the polarity score
if blob.sentiment.polarity >=0:
    print("You sound possitive")
elif blob.sentiment.polarity<0:
    print('You sound negative')