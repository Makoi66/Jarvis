import funcs
import win32com.client as wincl
import googletrans


def translate():
    translator = googletrans.Translator()
    text = str(funcs.voice)
    for x in funcs.opts["cmds"]["translator"]:
            text = text.replace((x), "").strip()
    print(text)
    result = translator.translate(text)
    try:
        print(result.text)
        spk = wincl.Dispatch("SAPI.SpVoice")
        vcs = spk.GetVoices()
        spk.Voice
        spk.SetVoice(vcs.Item(1))
        spk.Speak(result.text)
    except:
        funcs.speak("Не понял")