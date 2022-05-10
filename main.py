import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

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
        elif 'procure por' in comando:
            procurar = comando.replace('procure por', '')
            maquina.say("procurando por" + procurar)
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar,2)
            maquina.say(resultado)
            maquina.runAndWait()
        elif 'tocar' in comando:
            musica = comando.replace('tocar', '')
            resultado = pywhatkit.playonyt(musica)
            maquina.say("tocando a musica " + musica)
            maquina.runAndWait()

    comando_voz_usuario()