import mysql.connector as mysqlconn
from mysql.connector.errors import Error
import comandos_sql as comsql

try:
    connection = mysqlconn.connect(host='localhost',
                                   database='sol_nascente',
                                   user='root',
                                   password='Pi3,14159265')
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute()
        record = cursor.fetchone()
        print("connected database -> ", record)

except Error as e:
    print("error -> ", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("connection close")




