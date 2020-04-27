import speech_recognition as sr

from gtts import gTTS
from playsound import playsound
from googletrans import Translator
# Funcao responsavel por falar


def cria_audio(text, idioma):
    tts = gTTS(text, lang=idioma)
    # Salva o arquivo de audio
    tts.save('audios/text.mp3')
    print("Estou aprendendo o que você disse e traduzindo para minha língua...")
    # Da play ao audio
    playsound('audios/text.mp3')


# Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        # Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        # Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        # Armazena a informacao de audio na variavel
        audio = microfone.listen(source)
    with sr.Microphone() as source:
        print("Você deseja traduzir para qual idioma ?")
        audio2 = microfone.listen(source)

    try:
        # Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio, language='pt-BR')
        # Após alguns segundos, retorna a frase falada
        idioma = microfone.recognize_google(audio2, language='pt-BR')
        print("Você disse: " + frase + ". e o idioma de escolha foi: " + idioma)
        translator = Translator()
        if idioma == 'italiano':
            idioma = 'it'
            textotraduzido = translator.translate(frase, dest=idioma)
            cria_audio(textotraduzido.text, idioma)
        if idioma == 'alemão':
            idioma = 'de'
            textotraduzido = translator.translate(frase, dest=idioma)
            cria_audio(textotraduzido.text, idioma)
        if idioma == 'francês':
            idioma = 'fr'
            textotraduzido = translator.translate(frase, dest=idioma)
            cria_audio(textotraduzido.text, idioma)
        else:
            cria_audio("Não entendo essa língua, me desculpe !", "pt-br")

        # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnknownValueError:
        cria_audio("Não entendi", "pt-br")

    return frase


frase = ouvir_microfone()
