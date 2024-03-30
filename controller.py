import time
import flet as ft
import model as md
class SpellChecker:
    def handleSpellCheck(self, e):
        modalitaRicerca = self._view._searchModality.value
        lingua = self._view._selectLanguage.value
        if modalitaRicerca == None or lingua == None:
            self._view._lvOut.controls.clear()
            self._view._lvOut.controls.append(ft.Text("Non sono stati inseriti i valori richiesti", color="red"))
            self._view.update()
            return
        fraseInserita = self._view._txtIn.value
        if fraseInserita == "":
            self._view._lvOut.controls.clear()
            self._view._lvOut.controls.append(ft.Text("Non hai inserito nessuna frase!!!", color="red"))
            self._view.update()
            return
        multidizio = md.MultiDictionary()
        self._view._lvOut.controls.clear()
        self._view._txtIn.value = ""
        listaParole = fraseInserita.split(" ")
        paroleErrate, tempo = multidizio.printWord(listaParole, lingua, modalitaRicerca)
        self._view._lvOut.controls.append(ft.Text(f"Frase inserita: {fraseInserita}\nParole errate: - {paroleErrate}\nTempo richiesto dalla ricerca: {tempo}"))
        self._view.update()

    def _init_(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleChange1(self, e):
        self._view._lvOut.controls.append(ft.Text(f"Hai selezionato la lingua: {self._view._selectLanguage.value}"))
        self._view.update()

    def handleChange2(self, e):
        self._view._lvOut.controls.append(ft.Text(f"Hai selezionato il tipo di ricerca: {self._view._searchModality.value}"))
        self._view.update()
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
        print("__________\n" +
              "      SpellChecker 101\n"+
              "__________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "__________\n")


def replaceChars(text):
    chars = "\\`*{}[]()>#+-.!$?%^;,=~"
    for c in chars:
        text = text.replace(c, "")
    return text