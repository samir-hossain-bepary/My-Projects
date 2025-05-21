import pyttsx3

speaker = pyttsx3.init()

Text =input("Enter the text yo speak :")

speaker.say(Text)

speaker.runAndWait()