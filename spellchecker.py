import os
import time
import multiDictionary as md
import dictionary as d

def replace_chars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

class SpellChecker:

    def __init__(self):
        self._dict = md.MultiDictionary()
        self.load_dictionaries()

    def load_dictionaries(self):
        languages = {"italian": "Italian.txt", "english": "English.txt", "spanish": "Spanish.txt"}
        for lang, file in languages.items():
            pathfile = "resources/" + file
            if os.path.exists(pathfile):
                dictionary = d.Dictionary()
                dictionary.loadDictionary(pathfile)
                self._dict.add_dictionary(lang, dictionary)
            else:
                print(f"Warning: Il dizionario per {lang} ({pathfile}) non è stato trovato.")

    def handleSentence(self, txtIn, language):
        txtIn = replace_chars(txtIn.lower())
        words = txtIn.split()

        # Esegui la ricerca con entrambi i metodi e misura i tempi
        rich_words_linear, time_linear = self._dict.search_word_linear(words, language)
        rich_words_dichotomic, time_dichotomic = self._dict.search_word_binary(words, language)

        # Usa i risultati della ricerca dicotomica (più veloce)
        incorrect_words = [str(word) for word in rich_words_dichotomic if not word.is_corretta()]

        print(f"Parole errate: {incorrect_words}")
        print(f"Numero errori: {len(incorrect_words)}")
        print(f"\nConfronto tempi di esecuzione:")
        print(f"- Ricerca lineare: {time_linear:.6f} secondi")
        print(f"- Ricerca dicotomica: {time_dichotomic:.6f} secondi")
        print(f"- Miglioramento: {(time_linear / time_dichotomic if time_dichotomic > 0 else 0):.2f}x")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")