# Caucular a tabuada de qualquer valor
tabuada = int(input('Qual a tabuada de... '))

for x in range(1, 11):
    print('{0} x {1} = {2}'.format(x, tabuada, (tabuada * x)))
