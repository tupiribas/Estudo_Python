from contextlib import suppress
import conexao as conn
from pymongo import errors

db = conn.db_connect()['estudo_py']
tabela = db['clientes']


def inserir(nome='', idade=0, cpf=''):
    dados = {"nome": f"{nome}", "idade": idade, "cpf": f"{cpf}"}
    if (nome and idade and cpf):
        with suppress(errors.OperationFailure, errors.WriteConcernError):
            tabela.insert_one(dados)
            return 'Cliente incluido com sucesso!'
    else:
        return 'Valores nulos, tente novamente!'


def mostrar_todos():
    with suppress(errors.OperationFailure):
        for cliente in tabela.find():
            print(cliente)


def mostrar_com_filtro(dado):
    with suppress(errors.OperationFailure):
        for cliente in tabela.find():
            print(f'{cliente[dado]}')


def filtrar_tipo(tipo):
    if tipo == '_id':
        return '_id'
    elif tipo == 'nome':
        return 'nome'
    elif tipo == 'idade':
        return 'idade'
    else:
        return 'cpf'


def buscar_dado(tipo='', dado=''):
    with suppress(errors.OperationFailure,
                  errors.CollectionInvalid,
                  errors.InvalidOperation):
        doc = tabela.find({f"{filtrar_tipo(tipo)}": {"$regex": dado}})
        for cliente in doc:
            print(cliente)


# inserir('Tupiracy', 52, '233.231.321-01') foi
# mostrar_todos()
# mostrar_com_filtro('nome')
buscar_dado('nome', 'Guedes')
