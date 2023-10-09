from win32com.client import Dispatch

if __name__ == '__main__':

    # defining function
    def speak(text):
        speak = Dispatch("SAPI.SpVoice").Speak
        speak = Dispatch("SAPI.SpVoice").Speak
        speak(text)

    # welcome message for 1st time
    speak("Hello I am a speaking robot, write what ever you want me to say and to stop, kindly write a single alphabet q ")

    while True:
        print("Write what you want to speak:", end="")
        x = input()
        if x =='q':
            speak("Thank you for choosing me have a good day")
            break
        else:
            speak(x)

