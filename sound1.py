import funcs
from sound import Sound

def sound():
    text=str(funcs.voice)
    if "прибавь" or "увелич" in text:
        Sound.volue_up()