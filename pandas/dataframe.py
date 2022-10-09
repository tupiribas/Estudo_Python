import pandas as pd

calorico = {
    'calorias': [245, 344, 388],
    'duracao': [32, 60, 12]
}

cal = pd.DataFrame(calorico)
print(cal)

print('\nLocalizar linha')
print(cal.loc[[0, 1]])

print('\nIndice nomeado')
dados_cal = pd.Series(calorico, index=['dia1', 'dia2', 'dia3'])
print(dados_cal['dia2'])
