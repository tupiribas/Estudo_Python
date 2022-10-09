x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

# Escopo global


def teste():
    global x
    x = 300


teste()
print(x)
