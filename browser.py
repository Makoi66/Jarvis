import webbrowser
import random

import funcs

words=['Уже бегу!', 'Открываю', 'Запускаю', 'Сейчас', 'Сей момент']

def browser():
    sites = {"https://vk.com": ["vk", "вк"], 'https://www.youtube.com/': ['youtube', 'ютуб'],
             'https://ru.wikipedia.org': ["вики", "wiki"], 'https://ru.aliexpress.com': ['али', 'ali'],
             'https://google.com': ['гугл', 'google'], 'https://www.amazon.com': ['амазон', 'amazon'],
             'https://www.apple.com/ru': ['apple', 'эпл'], 'https://www.instagram.com': ['inst', 'инст',],
             'https://kpml.ru': ['школ', 'кфмл', 'kpml', 'фмл'], 'https://www.gismeteo.ru/': ['погод', 'прогноз'],
             'https://mail.google.com': ['почт', 'ящик'], 'https://yandex.ru': ['яндекс', 'yandex'],
             'http://kpml.ru:8080': ['дневник', 'электронный', 'журнал'], 'https://ria.ru/': ['новости']}
    site = funcs.voice
    for k, v in sites.items():
        for i in v:
            if i not in site.lower():
                open_tab = None
            else:
                open_tab = webbrowser.open_new_tab(k)
                funcs.speak(words[random.randint(0,3)])
                break

        if open_tab is not None:
            break
