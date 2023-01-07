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
        trans_output.delete(1.0, tk.END)
        trans_output.insert(1.0, f'{translation_machine(recent_value)}')
def run_listener(window, interval):
    check_clipboard()
    root.after(interval, run_listener, window, interval)

root = tk.Tk()

root.geometry('700x500')

root.title('Clipboard Translator')


translation_output = tk.Label(root,
                       text='Translated Output',
                       font=('Arial', 25),
                       padx=20)
translation_output.place(x=0, y=0)

trans_output = tk.Text(root,
                       font=('Arial', 15),
                       bg='white',
                       width=60,
                       padx=0,
                       height=19,
                       wrap='word',
                       )
trans_output.insert('1.0', 'Waiting for new translation...' )
# trans_output.bind('<Configure>', lambda e: trans_output.config(wraplength=trans_output.winfo_width()))
trans_output.place(x=20, y=50, anchor='nw')

run_listener(root, 500)


root.mainloop()
