from getdata import getdata

content = getdata.getdata('day2')
content = getdata.separarPorLineas(content)

correspondencia_oponente = {
    'A': 'r',
    'B': 'p',
    'C': 's',
}

puntuaciones_jugada = {
    'r': 1,
    'p': 2,
    's': 3,
}

def ganador(oponente: str, jugador: str) -> int:
    '''
    "r" -> rock
    "p" -> paper
    "s" -> scissors

    :param oponente: oponents play
    :param jugador: players play
    :return: winner (1 jugador, -1 oponente, 0 empate)
    '''

    if (oponente == 'r' and jugador == 'p') or (oponente == 'p' and jugador == 's') or (oponente == 's' and jugador == 'r'):
        return 1
    elif (oponente == 'p' and jugador == 'r') or (oponente == 's' and jugador == 'p') or (oponente == 'r' and jugador == 's'):
        return -1
    return 0

def jugada(oponente: str, resultado: int) -> str:
    '''
    "r" -> rock
    "p" -> paper
    "s" -> scissors

    -1 -> loss
    0 -> draw
    1 -> win

    :param oponente: oponents play
    :param resultado: result of the match
    :return: the play the player should make
    '''
    if resultado < 0:
        if oponente == 'r':
            return 's'
        elif oponente == 'p':
            return 'r'
        else:
            return 'p'

    if resultado > 0:
        if oponente == 'r':
            return 'p'
        elif oponente == 'p':
            return 's'
        else:
            return 'r'

    return oponente

def first_star(datos):
    correspondencia_jugador = {
        'X': 'r',
        'Y': 'p',
        'Z': 's'
    }
    puntuacion = 0
    for partida in datos:
        oponente = correspondencia_oponente[partida[0]]
        jugador = correspondencia_jugador[partida[-1]]

        puntuacion += puntuaciones_jugada[jugador]

        resultado = ganador(oponente, jugador)
        if resultado == 1:
            puntuacion += 6
        elif resultado == 0:
            puntuacion += 3
        else:
            puntuacion += 0
    return puntuacion

def second_star(datos):
    correspondencia_jugada = {
        'X': -1,
        'Y': 0,
        'Z': 1
    }
    puntuacion = 0
    for partida in datos:
        oponente = correspondencia_oponente[partida[0]]
        resultado = correspondencia_jugada[partida[-1]]

        jugador = jugada(oponente, resultado)
        puntuacion += puntuaciones_jugada[jugador]
        if resultado == 1:
            puntuacion += 6
        elif resultado == 0:
            puntuacion += 3
        else:
            puntuacion += 0
    return puntuacion

print(second_star(content))