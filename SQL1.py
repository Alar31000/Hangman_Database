import xlrd
import mysql.connector

loc = "WordDB50.xlsx"
index_mot = 0
mot_array = []

def insert_in_table(mot):
    try :
        connexion = mysql.connector.connect(user='root',
                                            password='Hurricaner2!',
                                            host='127.0.0.1',
                                            database='DB_Hangman')
        sql_insert_query = "''INSERT INTO words(words_id, mot, dico, difficulte) VALUES('', index_mot '' , '', mot '' , '', null '' , '', 1 '')''"
        cursor = connexion.cursor()
        connexion.commit()
        print(cursor.rowcount,"success")
        cursor.close()
        
    except mysql.connector.error as error
        print("success{}".format(error))
        
    finally :
        if(connexion.is_connected()):
            connexion.close()
            print("Connexion est fermée!")
            
def retrieve_words():
    for mot in mot_array :
        insert_in_table(mot)

def add_words():
    workbook = xlrd.open_workbook(loc)
    worksheet = workbook.sheet_by_index(0)
    cells = worksheet.row_slice(rowx=1,
                              start_colx=0,
                              end_colx=0)
    for cell in cells:
        mot_array.append(cell.value)
        print (\ncell.value," a été ajouté")