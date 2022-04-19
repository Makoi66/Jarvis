from __future__ import unicode_literals
import urllib.request
from urllib.parse import quote
import re
import webbrowser
import funcs
import pafy

def youtube():
    search_keyword = str(funcs.voice)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + quote(search_keyword))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=" + video_ids[0])
def music():
    search_keyword = str(funcs.voice)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + quote(search_keyword))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    ur = "https://www.youtube.com/watch?v=" + video_ids[0]
    video = pafy.new(ur)
    bestaudio = video.getbestaudio()
    bestaudio.download()