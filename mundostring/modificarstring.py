a = 'Hello world'
b = "Hello world"
c = '''Hi, my name is Tupi'''

# Maiusculas
print(a.upper())

# Minuscula
print(a.lower())

# Removedor de espaços em branco
# Retorna um list
print(a.split())
print(c.split(', '))

# Concatenar String
d = a[:5] + ' ' + b[5:]
print(d)
