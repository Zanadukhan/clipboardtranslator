import deepl
from deepl import Translator
import pyperclip
import sys
import tkinter as tk
import time
import os
from translationgui import TranslationGui

auth_key = "5630947a-19a7-cda6-995f-eff1c4e8a330:fx"
recent_value = ''

deepl_api = Translator(auth_key)

def translation_machine(input):
    translated_text = deepl_api.translate_text(f'{input}', target_lang='EN-GB')
    return str(translated_text)

def current_translation_limit():
    usage = deepl_api.get_usage()
    limit = f'Translation Limit:{usage.character.count}\{usage.character.limit}'
    return limit

def check_clipboard():
    global recent_value
    temp_value = pyperclip.paste()
    if temp_value != recent_value:
        recent_value = temp_value
        app.trans_output.delete(1.0, tk.END)
        app.trans_output.insert(1.0, f'{translation_machine(recent_value)}')
def run_listener(window, interval):
    check_clipboard()
    app.after(interval, run_listener, window, interval)


app = TranslationGui(current_translation_limit())

run_listener(app, 500)

app.mainloop()
