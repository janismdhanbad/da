from toneanalyser import tone1,tone2,tone3
from main import key1,key2,key3,key4,key5,key6
from gtts import gTTS

blabla = ("Hello Janpreet, you have received an important email, the tone of the mail is" + tone1 +"," + tone2 + "and" + tone3 + "and the keywords associated with it are" + key1 + "." + key2 + "." + key3 + "." + key4 + "." + key5 + "." + key6 + ".")
tts = gTTS(text=blabla, lang='en')
tts.save("test1.mp3")