import UserInterface.UserInterface as ui
import comandos_sql.comandos_create
from comandos_sql.connect import *

def executeSQLCommand(cursor, comando):
    cursor.execute(comando)



if __name__ == '__main__':
    connection = connector()
    cursor = connection.cursor()
    executeSQLCommand(cursor, comandos_sql.comandos_create.createTodos)
    closeConnector(connection, cursor)

