import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import sys
import datetime

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say("olá, eu sou a Lua")
while True:
    maquina.runAndWait()

    def executa_comando():
        try:
            with sr.Microphone() as source:
                print("Ouvindo...")
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language="pt-BR")
                comando = comando.lower()
                if 'lua' in comando:
                    comando = comando.replace('lua', '')
                    maquina.runAndWait()
    

                

        except:
            print("Microfone não está ok.")

        return comando

    def comando_voz_usuario():
        comando = executa_comando()
        if 'horas' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            maquina.say("Agora são" + hora)
            maquina.runAndWait()
      
        elif 'tocar' in comando:
            musica = comando.replace('tocar', '')
            resultado = pywhatkit.playonyt(musica)
            maquina.say("tocando a musica " + musica)
            maquina.runAndWait()

        elif 'encerrar programa' in comando:
            print("Programa encerrado, obrigado")
            sys.exit()

    comando_voz_usuario()