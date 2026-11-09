from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_generi(self):  # recupera tutti i geneti senza duplicati
        conn=DBConnect.get_connection()

        if conn is None:
            return []

        cursor=None
        try:
            cursor=conn.cursor()
            query='''SELECT DISTINCT genere
                    FROM libro
                    WHERE genere IS NOT NULL
                    '''
            cursor.execute(query)
            risultati=cursor.fetchall()
            generi=[]

            for riga in risultati:
                generi.append(riga[0])

            return generi

        finally:
            if cursor is not None:
                cursor.close()
            conn.close()

    def get_libri_filtrati(self,biblioteca,genere): # recupera i libri applicando i filtri selezionati
        conn=DBConnect.get_connection()
        if conn is None:
            return []

        cursor=None
        try:
            cursor=conn.cursor()
            query="""SELECT id,titolo,autore,genere,anno_pubblicazione,id_biblioteca
                    FROM libro
                    WHERE id_biblioteca=COALESCE(%s, id_biblioteca)
                    AND genere=COALESCE(%s,genere)"""

            cursor.execute(query,(biblioteca,genere))
            risultati=cursor.fetchall()

            libri=[]
            for riga in risultati:
                libro=Libro(
                            id=riga[0],
                            titolo=riga[1],
                            autore=riga[2],
                            genere=riga[3],
                            anno_pubblicazione=riga[4],
                            id_biblioteca=riga[5],
                        )
                libri.append(libro)

            return libri

        finally:
            if cursor is not None:
                cursor.close()
            conn.close()






