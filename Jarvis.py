import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import webbrowser

while 1:
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print('Available commands: "Play... (plays chosen song on youtube)", "Info about... (generates a wikipedia summary) ",\n "Shut down (shuts down PC)", "time (tells current time)", "open... (open website)", "search for... (searches for anything)"\n"exit (exits itself)"')
                
    def talk(text):
        engine.say(text)
        engine.runAndWait()


    def take_command():
        command = ""  
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'jarvis' in command:
                    command = command.replace('jarvis', '')
                    talk()
                    print(command)
        except:
            pass
        return command


        
    def run_jarvis():
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            print("playing" + song + "...")
            talk("playing " + song + "...")
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            talk('Current time is' + time)
            print(time)

        elif 'info about' in command:
            person = command.replace('info about', '')
            info = wikipedia.summary(person, 4)
            print(info)
            talk(info)

        elif 'shut down' in command:
            talk('Shutting down the computer...')
            os.system('shutdown /s /t 0')

        elif 'aesthetic' in command:
            talk('The most aesthetic person in the world is Leon Edwards.')
            print('The most aesthetic person in the world is Leon Edwards.')

        elif 'open' in command:
            url = command.replace('open', '')
            talk("Opening " + url + "...")
            print("Opening " + url + "...")
            webbrowser.open(url)

        elif 'search for' in command:
            query = command.replace('search for', '')
            pywhatkit.search(query)
            print(f'Searching for{query}.')

        elif command == 'exit':
            print("Goodbye! It was nice chatting with you.")
            talk("Goodbye! It was nice chatting with you.")
            exit()

        else:
            print("Please say the command again!")

        continuation = input("Press 'j' to call Jarvis again: ")
        if continuation != 'j':
            print("Goodbye! It was nice chatting with you.")
            talk("Goodbye! It was nice chatting with you.")
            exit()

    run_jarvis()
