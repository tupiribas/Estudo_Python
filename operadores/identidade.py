# OPERADORES...
'''
    5.Operadores de identidade:
'''

# Utilizados muito quando comparamos arrays (conjuntos)

# Is (Da ideia de "pertence" em algo)
x = ["pera", "banana"]
y = ["pera", "banana"]
z = x

print(x is z)
print(x in y)
print(x == y)

# Is not (inverso do is)
print(x is not z)
