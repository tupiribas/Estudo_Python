import meumodulo as meuM
import listapessoas as lp
from listapessoas import pessoas
import platform

meuM.imprimir_nome('Tupi')
pessoa1 = lp.pessoas['1']['nome']
print("Pessoa 1:", pessoa1)
pessoa2 = pessoas['1']['nome']
print("Pessoa 2:", pessoa2)

# Modulos integrados
x = platform.system()
# print(dir(platform))
print(x)
