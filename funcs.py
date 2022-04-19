import pyttsx3
import speech_recognition as sr
import os
from fuzzywuzzy import fuzz
import datetime
import win32com.client as wincl
import time
import keyboard

import anekdot
import browser
import calc
import convert
import translate
import music

opts = {"alias": ('дж', 'жарв', 'jahres', 'jar', 'арвис', 'гарвис', 'жарвис'),
        "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как', 'сколько', 'поставь', "засеки",
        'запусти', 'сколько будет',),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время'),
             "next": ('вперёд', 'дальш', 'следующий'),
             "back": ('обратн', 'назад', 'предыдущий'),
             'startStopwatch': ('запусти секундомер', "включи секундомер", "начини", "поставь секундомер"),
             'stopStopwatch': ('останови секундомер', "выключи секундомер", "выкл"),
             "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты', "шутк", 'анекдот'),
             "calc": ('прибав', 'умнож', 'разделить', 'степень', 'возведи' 'выч', 'подели', 'х', '+', '-', '/'),
             "shutdown": ('выключи компьютер', 'выключить компьютер', 'отключение компьютер', 'отключи питание', 'shutdown'),
             "sleep": ('сон', 'спящий режим'),
             "conv": ("валюта", "конвертер", "доллар", 'руб', 'евро'),
             "internet": ("открой", "сайт"),
             "translator": ("переведи", 'перевод'),
             "youtube": ("видео", 'запись', 'видео в', 'видео на', 'клип', 'фильм', 'открой клип', 'открой фильм', "открой видео"),
             # "music": ("песню", "трек", "симфонию"),
             "window": ('окн', 'переключи окно'),
             "winoff": ("сверн", 'закрой'),
             # "sound": ("гром", 'звук'),
             "deals": ("дела", "делишки", 'сам', 'жизнь')}}

startTime = 0
speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()
m = sr.Microphone(device_index=1)
voice = "str"



def speak(what):
    print(what)
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(what)

def callback(recognizer, audio):
    try:
        global voice
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)
        print(len(voice))
        if voice.startswith(opts["alias"]):
            cmd = voice
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            voice = cmd
            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            print(cmd)
            execute_cmd(cmd['cmd'])
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
        print("Говорите")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")



def listen():
    with m as source:
        print("Говорите")
        r.adjust_for_ambient_noise(source)
    stop_listening = r.listen_in_background(m, callback)
    while True:
        time.sleep(0.1)



def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 85}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.partial_ratio(cmd, x)
            if vrt >= RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC



def execute_cmd(cmd):
    global startTime
    print(cmd)
    if cmd == "next":
        keyboard.press("right arrow")
        keyboard.release("right arrow")
    elif cmd == "back":
        keyboard.press("left arrow")
        keyboard.release("left arrow")
    elif cmd == "winoff":
        keyboard.press("win")
        keyboard.press("D")
        keyboard.release("D")
        keyboard.release("win")
    elif cmd == "window":
        keyboard.press("alt")
        keyboard.press("tab")
        keyboard.release("tab")
        keyboard.release("alt")
    elif cmd == 'ctime':
        now = datetime.datetime.now()
        speak("Сейчас {0}:{1}".format(str(now.hour), str(now.minute)))
    elif cmd == 'startStopwatch':
        speak("Секундомер запущен")
        startTime = time.time()
    elif cmd == "stopStopwatch":
        if startTime != 0:
            Time = time.time() - startTime
            speak(f"Прошло {round(Time // 3600)} часов {round(Time // 60)} минут {round(Time % 60, 2)} секунд")
            startTime = 0
        else:
            speak("Секундомер не включен")
    elif cmd == 'calc':
        calc.calculator()
    elif cmd == 'conv':
        convert.convertation()
    elif cmd == 'translator':
        translate.translate()
    elif cmd == 'stupid1':
        anekdot.fun()
    elif cmd == 'youtube':
        music.youtube()
    elif cmd == 'music':
        music.music()
    elif cmd == 'internet':
        browser.browser()
    elif cmd == 'shutdown':
        os.system('shutdown -s -t 0')
        speak("Выключаю...")
    elif cmd == 'sleep':
        os.system('rundll32 powrprof.dll,SetSuspendState 0,1,0')
    elif cmd == 'deals':
        speak("Голова пока цела. Я имею ввиду процессор.")
    else:
        print("Команда не распознана")
    print("Говорите")
