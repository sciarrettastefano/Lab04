import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, e):
        # Faccio i controlli che tutto sia stato selezionato
        language = self._view._ddLanguage.value
        if language == None:
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Selezionare una lingua.", color="red")
            )
            self._view.update()
            return

        modality = self._view._ddModality.value
        if modality == None:
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Selezionare una modalità.", color="red")
            )
            self._view.update()
            return

        txtIn = self._view._txtIn.value
        if txtIn == "":
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Inserire una frase.", color="red")
            )
            self._view.update()
            return

        # Stampo nella lv la frase
        self._view._txtOut.controls.append(
            ft.Text(f"Frase inserita: {txtIn}")
        )

        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = ""
        tempoImpiegato = 0.0

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                tempoImpiegato = t2 - t1
                print(paroleErrate, t2 - t1)

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                tempoImpiegato = t2 - t1
                print(paroleErrate, t2 - t1)

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                tempoImpiegato = t2 - t1
                print(paroleErrate, t2 - t1)

        # Aggiungo alla lv le parole errate e il tempo impiegato
        self._view._txtOut.controls.append(
            ft.Text(f"Parole errate: {paroleErrate}")
        )
        self._view._txtOut.controls.append(
            ft.Text(f"Tempo richiesto alla ricerca: {tempoImpiegato}")
        )
        self._view.update()

    def handleClear(self, e):
        self._view._txtOut.controls.clear()
        self._view.update()

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text