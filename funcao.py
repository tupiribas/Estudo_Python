# Aprendendo a aplicar funções
def imprimir_nome_1(nome):
    return nome


print(imprimir_nome_1('Tupi Guedes Ribas'))


def imprimir_nome_2(nome):
    print(nome)


imprimir_nome_2('Tupi Guedes')


def calculadora(n1=0, n2=0, tipo=''):
    # Padronizacao PEP 8 -> (n1=0, n2=0, tipo='')
    if tipo == '+':
        return n1 + n2
    elif tipo == '-':
        return n1 - n2
    elif tipo == '*':
        return n1 * n2
    elif tipo == '/':
        return n1 / n2
    else:
        return 0


print(calculadora(2, 3, '+'))
print(calculadora(2, 3, '-'))
print(calculadora(2, 3, '*'))
print(calculadora(2, 3, '/'))
