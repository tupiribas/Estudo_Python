def hora_certa(horario): return horario.strftime("%H:%M:%S")
def manha(horario): return '06:00:00' < horario < '11:59:00'
def tarde(horario): return '12:00:00' < horario < '17:59:00'
def noite(horario): return '18:00:00' < horario < '23:59:00'
def madrugada(horario): return '00:00:00' < horario < '05:59:00'


def periodo(horario):
    if manha(hora_certa(horario)):
        return 'Bom dia'
    elif tarde(hora_certa(horario)):
        return 'Boa tarde'
    elif noite(hora_certa(horario)):
        return 'Boa noite'
    elif madrugada(hora_certa(horario)):
        return 'Boa madrugada'
