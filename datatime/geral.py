from datetime import datetime as dt
from diadasemana import por_extenso
from horadodia import periodo

agora = dt.now()

data_padrao_br_01 = (agora.date()).strftime('%d/%m/%Y')
mes_por_extenso = (agora.date()).strftime('%B')
dia_da_semana = por_extenso(1)
momento_do_dia = periodo(agora)
momento_sem_saudacao = momento_do_dia.split(' ')[1]

hora = agora.hour
minuto = agora.minute

print(f'{momento_do_dia} Tupi!')
print(f'Hoje já e {dia_da_semana}, {data_padrao_br_01} ás {hora}:{minuto}')
print(f'da {momento_sem_saudacao}')
