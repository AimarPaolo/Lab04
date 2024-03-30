import time
import flet as ft
import model as md
class SpellChecker:
    def handleSpellCheck(self, e):
        multidizio = md.MultiDictionary()
        self._view._lvOut.controls.clear()
        fraseInserita = self._view._txtIn.value
        self._view._txtIn.value = ""
        modalitaRicerca = self._view._searchModality.value
        lingua = self._view._selectLanguage.value
        listaParole = fraseInserita.split(" ")
        paroleErrate, tempo = multidizio.printWord(listaParole, lingua, modalitaRicerca)
        if modalitaRicerca == None or lingua == None:
            self._view._lvOut.controls.append(ft.Text("Non sono stati inseriti i valori richiesti", color="red"))
            self._view.update()
            return
        self._view._lvOut.controls.append(ft.Text(f"Frase inserita: {fraseInserita}\nParole errate: - {paroleErrate}\nTempo richiesto dalla ricerca: {tempo}"))
        self._view.update()

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


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


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text