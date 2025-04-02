import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!
    try:
        if int(txtIn) == 1:
            print("Inserisci la tua frase in Italiano\n")
            txtIn = input()
            sc.handleSentence(txtIn,"italian")
            continue

        if int(txtIn) == 2:
            print("Inserisci la tua frase in Inglese\n")
            txtIn = input()
            sc.handleSentence(txtIn,"english")
            continue

        if int(txtIn) == 3:
            print("Inserisci la tua frase in Spagnolo\n")
            txtIn = input()
            sc.handleSentence(txtIn,"spanish")
            continue

        if int(txtIn) == 4:
            print("Esci dal programma.")
            break

    except ValueError:
        print("Input non valido. Per favore, inserisci un numero tra 1 e 4.")
        continue

