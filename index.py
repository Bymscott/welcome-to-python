from random import randint
import mysql.connector as sql

class BankConfiguration:

    __mycursor = None
    __conn = None
    u_id = None


    def __init__(self):
        self.__conn = sql.connect(

            host = 'localhost',
            port = '3306',
            user = 'root',
            password = '',
            db = 'september_db'

        )