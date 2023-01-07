import tkinter as tk

class TranslationGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x500')
        self.title('Clipboard Translator')

        self.translation_output = tk.Label(self,
                                           text='Translated Output',
                                           font=('Arial', 25),
                                           padx=20)
        self.translation_output.place(x=0, y=0)

        self.trans_output = tk.Text(self,
                                    font=('Arial', 15),
                                    bg='white',
                                    width=60,
                                    padx=0,
                                    height=19,
                                    wrap='word',
                                    )
        self.trans_output.insert('1.0', 'Waiting for new translation...')
        self.trans_output.place(x=20, y=50, anchor='nw')