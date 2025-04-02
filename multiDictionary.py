from re import search

import dictionary as d
import richWord as rw
import time

class MultiDictionary:

    def __init__(self):
       self.dictionaries = {}

    def add_dictionary(self, language, dictionary):
        self.dictionaries[language] = dictionary

    def printDic(self, language):
        pass

    def search_word(self, words, language):
        """Metodo generico che utilizza l'operatore 'in'."""
        if language not in self.dictionaries:
            print(f"Dizionario per {language} non disponibile.")
            return []

        dictionary = self.dictionaries[language]
        rich_words = []
        for word in words:
            rich_word = rw.RichWord(word)
            rich_word.set_corretta(word in dictionary)
            rich_words.append(rich_word)
        return rich_words

    def search_word_linear(self, words, language):
        """Utilizza la ricerca lineare."""
        if language not in self.dictionaries:
            print(f"Dizionario per {language} non disponibile.")
            return []

        dictionary = self.dictionaries[language]
        rich_words = []
        start_time = time.time()

        for word in words:
            rich_word = rw.RichWord(word)
            rich_word.set_corretta(dictionary.search_linear(word))
            rich_words.append(rich_word)

        end_time = time.time()
        search_time = end_time - start_time

        return rich_words, search_time

    def search_word_binary(self, words, language):
        """Utilizza la ricerca binaria."""
        if language not in self.dictionaries:
            print(f"Dizionario per {language} non disponibile.")
            return []

        dictionary = self.dictionaries[language]
        rich_words = []
        start_time = time.time()

        for word in words:
            rich_word = rw.RichWord(word)
            rich_word.set_corretta(dictionary.search_binary(word))
            rich_words.append(rich_word)

        end_time = time.time()
        search_time = end_time - start_time

        return rich_words, search_time