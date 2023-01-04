from deepl import Translator
import pyperclip
import sys
import tkinter as tk
import time
import os
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

root.geometry('700x300')

root.title('Clipboard Translator')

clipboard_title = tk.Label(root,
                           text='Clipboard Translator',
                           font=('Arial', 25),
                           padx=20)

clipboard_title.place(x=0, y=0)

current_clipboard = tk.Label(root,
                             textvariable=paste,
                             font=('Arial', 15),
                             bg='white',
                             width=60,
                             # height=2,
                             anchor='nw',
                             justify='left',
                             padx=0,
                             )
current_clipboard.bind('<Configure>', lambda e: current_clipboard.config(wraplength=current_clipboard.winfo_width()))
current_clipboard.place(x=20, y=50)

translation_output = tk.Label(root,
                       text='Translated Output',
                       font=('Arial', 25),
                       padx=20)
translation_output.place(x=0, y=140)

trans_output = tk.Label(root,
                        textvariable=translation,
                        font=('Arial', 15),
                        bg='white',
                        width=60,
                        height=2,
                        anchor='nw',
                        justify='left',
                        padx=0,
                        )
trans_output.bind('<Configure>', lambda e: trans_output.config(wraplength=trans_output.winfo_width()))
trans_output.place(x=20, y=190)


run_listener(root, 500)


root.mainloop()
