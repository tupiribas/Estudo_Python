# Tipos de Strings
a = 'Hello world'
b = "Hello world"
c = '''
    Hi, my name is Tupi
'''
print(a)
print(b)
print('Texto:', c)

# Fatiar Strings - o primeiro caracter tem indice -> (a[0]) o intervalo começa
# no primeiro caracte
# Inicio e o Fim
print(a[2:3])
print(b[2:5])

# Desde o inicio...
print(a[1:])
print(b[5:])

# ...até o Fim
print(a[:5])
print(b[:1])

# Negativo (Começa sempre do maior para o menor valor)([-10:-5])
print(a[-5:-1])
