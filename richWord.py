class RichWord:
    def __init__(self, parola):
        self._parola = parola # this is a string
        self._corretta = False #this is a bool

    def is_corretta(self):
        # print("getter of parola called" )
        return self._corretta

    def set_corretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        return self._parola