import os

# a - anexar ao final do arquivo
# w - substitui qualquer conteudo existente
pasta = './manipulacao_arquivos/'
path = './manipulacao_arquivos/demostracao02.txt'
# f = open(path, 'w')
# f.write('Adoraria ser mais feliz do que ja sou.')
# f = open(path, 'r')
# print(f.read())
# f.close()

# # f = open(pasta + 'demonstracao03.txt', 'x')
# f.close()
# f = open(pasta + 'demonstracao03.txt', 'w')
# f.write('Adoro criar aquivos com python!')

# f = open(pasta + 'demonstracao03.txt', 'r')
# print(f.read())

# Excluir aquivos
os.remove(pasta + 'demonstracao03.txt')
os.remove(pasta + 'demostracao.txt')
