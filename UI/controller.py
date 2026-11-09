import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self): #recupera dal model tutte le biblioteche,tutti i generi
        biblioteche=self._model.get_biblioteche()
        generi=self._model.get_generi()

        self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(key='Nessun filtro',text='Nessun filtro'))

        for biblioteca in biblioteche:
            self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(key=str(biblioteca.id),text=biblioteca.nome))

        self._view.dropdown_genere.options.append(
            ft.dropdown.Option(key="Nessun filtro",text='Nessun filtro')
        )

        for genere in generi:
            self._view.dropdown_genere.options.append(ft.dropdown.Option(key=genere,text=genere))


        self._view.update()
    # CALLBACKS DROPDOWN
    # TODO
    def seleziona_biblioteca(self,e): #quando utente seleziona una bibliotaca, memorizziamo il suo id
                                                #se seleziona 'nessun filtro' memeorizziamo None
        if e.control.value=='Nessun filtro':
            self.biblioteca_selezionata=None
        else:
            self.biblioteca_selezionata=int(e.control.value)

    def seleziona_genere(self,e): # memorizziamo il genere selezionato oppure None
        if e.control.value=='Nessun filtro':
            self.genere_selezionato=None
        else:
            self.genere_selezionato=e.control.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self,e): #
        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato
        )

        self._view.lista_libri.controls.clear() # svuota la lista

        if len(libri) == 0: # controlla se ci sono libri
            self._view.show_alert("Nessun libro trovato")
        else:
            for libro in libri: # scorre tutti i libri trovati
                self._view.lista_libri.controls.append(
                    ft.Text(str(libro))
                )

        self._view.update()


