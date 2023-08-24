import speech_recognition as sr,pyaudio

mic = sr.Microphone(1)
recog = sr.Recognizer()

with mic as source:
    print("เริ่ม")
    audio = recog.listen(source)
    print(str(recog.recognize_google(audio, language="th")))
    