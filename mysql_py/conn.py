import mysql.connector as conn
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

load_dotenv()


def coneccao(nome):
    return os.environ[nome]


def conexao():
    try:
        mydb = conn.connect(
            host=coneccao('host'),
            user=coneccao('user'),
            password=coneccao('password'),
            database=coneccao('database')
        )
        return mydb
    except conn.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Esse banco de dados nao existe")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("O nome ou senha talvez esteja incorreto")
        else:
            print(error)


def fechar_conexao(connection):
    connection.close()
