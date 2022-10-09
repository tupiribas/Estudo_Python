# Tipos de dados (Cola)
'''
Tipo de texto:	    str
Tipos Numéricos:	int, float, complex
Tipos de sequência:	list, tuple, range
Tipo de mapeamento:	dict
Tipos de conjunto:	set,frozenset
Tipo booleano:	    bool
Tipos binários:	    bytes, bytearray, memoryview
Nenhum Tipo:	    NoneType
'''
x = 'hello world'
y = '1234'
z = 1234
log = True

# Muda o tipo
print(str(x))
print(int(y))
print(float(z))
# Outra possibilidade
print(float(y))
# Faz parte do conjunto dos complexos
print(type(1j))
# Tipos de array
print(type([x, y, z]))
print(type({'x': x, 'y': y, 'z': z}))
print(type((x, y, z)))
print(type({x, y, z}))
print(type(frozenset({x, y, z})))
# Tipos de dados
print(type(log))
print(type(b'Hello'))
# Conta quantos bytes consome um determinado array
print(bytearray(x.__len__()))
# Local onde esta sendo armazeado a variavel
print(memoryview(bytes(x.__len__())))
print(memoryview(bytes(y.__len__())))
print(memoryview(bytes(z)))
print(memoryview(bytes(log)))

# Sequencia de valores
r = range(1, 6)
for num in r:
    print(num)

# Converter numeros:
i = 1
m = 2.8
n = 1j

# Int >>> Float
a = float(i)

# Float >>> Int
b = int(m)

# Int >>> Complex
c = complex(n)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
