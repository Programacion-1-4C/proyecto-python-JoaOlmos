import random

def ver_tablero():
    print("\n")
    print(tablero[6] + " | " + tablero[7] + " | " +  tablero[8]  +"       7 | 8 | 9")
    print(tablero[3] + " | " + tablero[4] + " | " +  tablero[5]  +"       4 | 5 | 6")
    print(tablero[0] + " | " + tablero[1] + " | " +  tablero[2]  +"       1 | 2 | 3")
    print("\n")

def jugar():
    Ganador = None
    print("Empieza el juego!")
    ver_tablero()
    for i in range(5):
        if Ganador == "O":
            break
        print("Turno del jugador 1 - X")
        valor="X"
        #empiezan a jugar - Jugador1

        Anoto = False
        while not Anoto:
            posicion = int(input("Elegi una posicion del 1 al 9: "))
            posicion -= 1
            if tablero[posicion] == "-":
                Anoto = True
            else:
                print("Esa posicion ya esta ocupada")
        tablero[posicion] = valor
        ver_tablero()

        if tablero[0] == tablero[1] == tablero[2] != "-":
            Ganador = tablero[0]
        elif tablero[3] == tablero[4] == tablero[5] != "-":
            Ganador = tablero[3]
        elif tablero[6] == tablero[7] == tablero[8] != "-":
            Ganador = tablero[6]
        elif tablero[0] == tablero[3] == tablero[6] != "-":
            Ganador = tablero[0]
        elif tablero[1] == tablero[4] == tablero[7] != "-":
            Ganador = tablero[1]
        elif tablero[2] == tablero[5] == tablero[8] != "-":
            Ganador = tablero[2]
        elif tablero[0] == tablero[4] == tablero[8] != "-":
            Ganador = tablero[0]
        elif tablero[2] == tablero[4] == tablero[6] != "-":
            Ganador = tablero[2]

        if Ganador != "X" and i < 4 :
            for j in range(3):
                print("Turno de la AI - O")
                valor="O"
                Anoto = False
                while not Anoto:
                    if tablero[4] == "-":
                        tablero[4] = valor
                        Anoto = True
                    else:
                        while True:
                            while True:
                                posicion = random.randint(0, 8)
                                if tablero[posicion] == "-":
                                    tablero[posicion] = valor
                                    Anoto = True
                                    break
                                else:
                                    break
                            if tablero[posicion] == valor:
                                break
                ver_tablero()

                if tablero[0] == tablero[1] == tablero[2] != "-":
                    Ganador = tablero[0]
                elif tablero[3] == tablero[4] == tablero[5] != "-":
                    Ganador = tablero[3]
                elif tablero[6] == tablero[7] == tablero[8] != "-":
                    Ganador = tablero[6]
                elif tablero[0] == tablero[3] == tablero[6] != "-":
                    Ganador = tablero[0]
                elif tablero[1] == tablero[4] == tablero[7] != "-":
                    Ganador = tablero[1]
                elif tablero[2] == tablero[5] == tablero[8] != "-":
                    Ganador = tablero[2]
                elif tablero[0] == tablero[4] == tablero[8] != "-":
                    Ganador = tablero[0]
                elif tablero[2] == tablero[4] == tablero[6] != "-":
                    Ganador = tablero[2]

                if Ganador == "O":
                    print("AI GANADOR del TA-TE-TI")
                    break
                else:
                    break
        elif Ganador == "X":
            print("Felicidadesss!!! Jugador 1 GANADOR del TA-TE-TI")
            break
        else:
            print("Empataron del TA-TE-TI")



tablero =[  "-", "-", "-",
             "-", "-", "-",
              "-", "-", "-"]