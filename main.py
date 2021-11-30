import UserInterface.UserInterface as ui
import comandos_sql.comandos_create
from comandos_sql.connect import *



if __name__ == '__main__':
    connection = connector()
    cursor = connection.cursor()
    closeConnector(connection, cursor)

