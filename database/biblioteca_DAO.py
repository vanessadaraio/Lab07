from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_biblioteche(self):
        conn=DBConnect.get_connection()

        if conn is None:
            return []

        cursor=None
        try:
            cursor=conn.cursor()
            query="""SELECT id,nome,indirizzo 
                    FROM biblioteca"""
            cursor.execute(query)
            risultati=cursor.fetchall()  # recupera tutte le righe trovate

            biblioteche=[]
            for riga in risultati: # trasformiamo i dati provenienti da MySQL in oggetti Python
                biblioteca=Biblioteca(id=riga[0],
                                      nome=riga[1],
                                      indirizzo=riga[2])
                biblioteche.append(biblioteca)

            return biblioteche
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()


