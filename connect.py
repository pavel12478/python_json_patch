import mysql.connector
from mysql.connector import Error
from config import host, user, passwd, db_name


def create_connection(host_name, user_name, user_password, name_db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=name_db
        )
        # print('Connection to database successfully')
    except Error as er:
        print(f"The error '{er}' occurred")
    return connection


connection = create_connection(host, user, passwd, db_name)
