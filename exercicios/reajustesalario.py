def texto_principal():
    print('''
        Abaixo de R$500,00       -> reajsute de 15%
        Entre R$500,00 R$1000,00 -> reajsute de 10%
        Acima de R$1000,00       -> reajsute de 5%
    ''')


texto_principal()

salario = float(input('Qual seu salario atual? '))

if salario < 500:
    novo_salario = salario + (salario * 0.15)
    print('Seu salario alterado em 15%: {0:.2f}'.format(novo_salario))
elif salario >= 500 and salario < 1000:
    novo_salario = salario + (salario * 0.10)
    print('Seu salario alterado em 10%: {0:.2f}'.format(novo_salario))
else:
    novo_salario = salario + (salario * 0.5)
    print('Seu salario foi alterado em 5%: {0:.2f}'.format(novo_salario))
