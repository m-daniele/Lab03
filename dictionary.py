class Dictionary:
    def __init__(self):
        self._general_dict = set()
        self._sorted_list = []

    def loadDictionary(self,path):
        try:
            with open(path, "r",encoding="utf-8") as infile:
                for line in infile:
                    self._general_dict.add(line.strip().lower())
            # Creiamo una lista ordinata per la ricerca dicotomica
            self._sorted_list = sorted(list(self._general_dict))
        except FileNotFoundError:
            print(f"File {path} not found")
            return

    def printAll(self):
        for word in self._general_dict:
            print(f"{word}\n")

    def search_linear(self, word):
        """Ricerca lineare nella lista ordinata."""
        for dictionary_word in self._sorted_list:
            if dictionary_word == word:
                return True
        return False

    def search_binary(self, word):
        """Ricerca binaria nella lista ordinata."""
        low = 0
        high = len(self._sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if self._sorted_list[mid] == word:
                return True
            elif self._sorted_list[mid] < word:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def __contains__(self, word):
        return word in self._general_dict

    @property
    def dict(self):
        return self._general_dict

