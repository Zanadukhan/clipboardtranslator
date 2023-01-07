from deepl import Translator
import pyperclip
import sys
import tkinter as tk
import time
import os
from translationgui import TranslationGui

auth_key = "insert api key here"
recent_value = ''

deepl_api = Translator(auth_key)

def translation_machine(input):
    translated_text = deepl_api.translate_text(f'{input}', target_lang='EN-GB')
    return str(translated_text)

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

app = TranslationGui()

run_listener(app, 500)


app.mainloop()
