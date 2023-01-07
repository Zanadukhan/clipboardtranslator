from deepl import Translator
import pyperclip
import sys
import tkinter as tk
import time
import os
auth_key = "insert auth key here"
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
        paste.set(recent_value)
        translation.set(translation_machine(recent_value))

def run_listener(window, interval):
    check_clipboard()
    root.after(interval, run_listener, window, interval)

root = tk.Tk()

paste = tk.StringVar()
paste.set(pyperclip.paste())

translation = tk.StringVar()
translation.set(translation_machine(pyperclip.paste()))

root.geometry('700x500')

root.title('Clipboard Translator')


translation_output = tk.Label(root,
                       text='Translated Output',
                       font=('Arial', 25),
                       padx=20)
translation_output.place(x=0, y=0)

trans_output = tk.Label(root,
                        textvariable=translation,
                        font=('Arial', 15),
                        bg='white',
                        width=60,
                        anchor='nw',
                        justify='left',
                        padx=0,
                        )
trans_output.bind('<Configure>', lambda e: trans_output.config(wraplength=trans_output.winfo_width()))
trans_output.place(x=20, y=50)


run_listener(root, 500)


root.mainloop()
