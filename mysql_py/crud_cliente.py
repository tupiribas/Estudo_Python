import conn
import numpy as np

bd = conn.conexao()


def criar_usuario(nome, idade):
    sql = "INSERT INTO cliente(nome,idade) VALUES ('{0}','{1}')".format(
        nome, idade)
    try:
        bd._open_connection()
        my_db = bd.cursor()

        my_db.execute(sql)
        return 'Cliente adicionado com sucesso!'
    except conn.errorcode as error:
        print(f'Erro ao criar usuario >>> \n{error}')
        return 'Nao foi possivel adicionar este cliente.'
    finally:
        conn.fechar_conexao(bd)


def mostrar_tudo():
    sql = 'SELECT * FROM cliente'
    try:
        bd._open_connection()
        my_db = bd.cursor()

        my_db.execute(sql)

        if my_db.rowcount < 0:
            resultado = my_db.fetchall()
            arr = np.array(resultado)
            return arr
    except conn.errorcode as error:
        print(f'Erro ao criar \n{error}')
    finally:
        conn.fechar_conexao(bd)


def buscar_por_id(id):
    sql = "SELECT * FROM cliente WHERE id = %s"
    try:
        bd._open_connection()
        my_db = bd.cursor()

        my_db.execute(sql, (id,))

        if my_db.rowcount < 0:
            resp = np.array(my_db.fetchall())
            return resp.reshape(-1)
    except conn.errorcode as error:
        print(f'Erro ao criar \n{error}')
    finally:
        conn.fechar_conexao(bd)


def filtrar_por_categoria(categoria, tipo='ASC'):
    sql = "SELECT * FROM cliente ORDER BY %s %s" % (categoria, tipo.upper())
    try:
        bd._open_connection()
        my_db = bd.cursor()

        my_db.execute(sql)
        resultado = my_db.fetchall()
        arr = np.array(resultado)
        return arr
    except conn.errorcode as error:
        print(f'Erro ao criar \n{error}')
    finally:
        conn.fechar_conexao(bd)


def excluir_por_id(id):
    sql = 'DELETE FROM cliente WHERE id = %s'
    try:
        bd._open_connection()
        my_db = bd.cursor()

        if my_db.rowcount < 0 and buscar_por_id(id) != []:
            my_db.execute(sql, (id,))
            bd.commit()
            return 'Cliente deletado com sucesso!'
        else:
            return 'Nao foi possivel alterar os dados desse usuario.'
    except conn.errorcode as error:
        print(f'Erro ao criar \n{error}')
    finally:
        conn.fechar_conexao(bd)


# print(criar_usuario('Tupi', 20))
print(criar_usuario('Carlos', 12))
