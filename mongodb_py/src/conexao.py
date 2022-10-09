from pymongo import MongoClient
from pymongo import errors
from dotenv import load_dotenv
from os import environ

load_dotenv()


def env(nome):
    return environ[nome]


def db_connect():
    try:
        conn = MongoClient(env('conn'))
        return conn
    except errors.ConnectionFailure as e:
        return 'Falha na conexao. >>> ', e
