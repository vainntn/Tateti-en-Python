tablero = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def dibujar_tablero(tablero):
    """Dibuja el tablero en pantalla."""
    print("     1   2   3")
    for i, row in enumerate(tablero):
        print(i + 1, end='  ')
        for col in row:
            print("|", col, end=' ')
        print("|")

def poner_ficha(ficha):
    """Coloca la ficha en la posición elegida por el usuario.
    Verifica que la posición sea correcta y que no esté ocupada.
    """
    ficha_ok = False
    while not ficha_ok:
        print("Turno:", ficha)
        try:
            fila = int(input("Seleccione una fila (1-3):")) - 1
            col = int(input("Seleccione una columna (1-3):")) - 1
            if tablero[fila][col] not in ('X', 'O'):
                tablero[fila][col] = ficha
                ficha_ok = True
            else:
                print("La posición ya está ocupada!")
                ficha_ok = False
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print("Posición incorrecta!")
            ficha_ok = False

def validar_tablero(tablero):
    """Valida el tablero para ver si el juego terminó
    con un ganador o terminó en empate o si todavía continua.
    -1: continua
    0: empate
    1: Gano O
    2: Gano X
    """
    resultado = -1
    # Fila completa
    regla_1 = (tablero[0][0] in ('X', 'O')) and (tablero[0][0] == tablero[0][1] == tablero[0][2])
    regla_2 = (tablero[1][0] in ('X', 'O')) and (tablero[1][0] == tablero[1][1] == tablero[1][2])
    regla_3 = (tablero[2][0] in ('X', 'O')) and (tablero[2][0] == tablero[2][1] == tablero[2][2])
    # Columna completa
    regla_4 = (tablero[0][0] in ('X', 'O')) and (tablero[0][0] == tablero[1][0] == tablero[2][0])
    regla_5 = (tablero[0][1] in ('X', 'O')) and (tablero[0][1] == tablero[1][1] == tablero[2][1])
    regla_6 = (tablero[0][2] in ('X', 'O')) and (tablero[0][2] == tablero[1][2] == tablero[2][2])
    # diagonales
    regla_7 = (tablero[0][0] in ('X', 'O')) and (tablero[0][0] == tablero[1][1] == tablero[2][2])
    regla_8 = (tablero[0][2] in ('X', 'O')) and (tablero[0][2] == tablero[1][1] == tablero[2][0])

    if regla_1:
        resultado = 2 if tablero[0][0] == 'X' else 1
    elif regla_2:
        resultado = 2 if tablero[1][0] == 'X' else 1
    elif regla_3:
        resultado = 2 if tablero[2][0] == 'X' else 1
    elif regla_4:
        resultado = 2 if tablero[0][0] == 'X' else 1
    elif regla_5:
        resultado = 2 if tablero[0][1] == 'X' else 1
    elif regla_6:
        resultado = 2 if tablero[0][2] == 'X' else 1
    elif regla_7:
        resultado = 2 if tablero[0][0] == 'X' else 1
    elif regla_8:
        resultado = 2 if tablero[0][2] == 'X' else 1
    else:
        empate = True
        for row in tablero:
            for col in row:
                if col not in ('X', 'O'):
                    empate = False
                    break;
        if empate:
            resultado = 0
    return resultado

print("TA-TE-TI")
termino = False
jugadas = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
dibujar_tablero(tablero)
while not termino:
    ficha = jugadas.pop()
    poner_ficha(ficha)
    dibujar_tablero(tablero)
    status = validar_tablero(tablero)
    if status == 1:
        termino = True
        print("Ganó O!")
    elif status == 2:
        termino = True
        print("Ganó X!")
    elif status == 0:
        termino = True
        print("La partida terminó en empate!")