from translate import Translator

user_input = input("Enter the text : ")

languages = {1: "en", 2: "es", 3: "pt", 4: "zh"}

while True:
    selected_lang = int(
        input("Translate in 1) English 2) Spanish 3) Portugese 4) Chinese : ")
    )
    if selected_lang in languages:
        Translator = Translator(to_lang=languages[selected_lang])
        break
    else:
        print("Please selec & valid  option!")
        continue

translation = Translator.translate(user_input)
print(translation)