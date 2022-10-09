nome = 'Tupi'
idade = 19
texto1 = 'My name is ' + nome + ' and I am ' + str(idade)
# Para garantir que os dados sejam colocados corretamente {numero}
texto2 = 'My name is {0} and I am {1}'

print(texto1)
print(texto2.format(nome, idade))
