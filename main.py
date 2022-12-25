from deepl import Translator
import pyperclip

auth_key = "5630947a-19a7-cda6-995f-eff1c4e8a330:fx"

translator = Translator(auth_key)

translate = True

while translate:
    pyperclip.waitForNewPaste()
    translated_text = translator.translate_text(f'{pyperclip.paste()}', target_lang='EN-GB')

    print(translated_text)
