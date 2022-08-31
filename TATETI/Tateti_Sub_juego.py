import time
from random import choice

contador = 0
contenido = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890!#$%&=?¿"
confirmarJ = True
TurnoJugador1 = True


def sub_juego():
    print("Empezamos Jugador 1")
    while True:
        while True:
            print("Jugador 1, escriba el siguiente simbolo o letra, en menos de 3 segundos")
            aux = (choice(contenido))
            print(aux)
            ls = input()  # letra_simbolo
            for i in contenido:
                if confirmarJ == False:
                    print("Te tardaste mucho!")
                    break
                elif ls == i and ls == aux:
                    print("Bien, Acertaste!")
                    break
            if confirmarJ == False:
                break
            elif ls == i:
                break
            elif ls != i:
                print("Fallaste")
                break
        if confirmarJ == False:
            break
        elif ls == i:
            break
        while True:
            print("Jugador 2, escriba el siguiente simbolo o letra, en menos de 3 segundos")
            aux = (choice(contenido))
            print(aux)
            ls = input()  # letra_simbolo
            for i in contenido:
                if confirmarJ == False:
                    print("Te tardaste mucho!")
                    break
                elif ls == i and ls == aux:
                    print("Bien, Acertaste!")
                    break
            if confirmarJ == False:
                break
            elif ls == i:
                break
            elif ls != i:
                print("Fallaste")
                break
        if confirmarJ == False:
            break
        if ls == i:
            TurnoJugador1 = False
            return TurnoJugador1


def cuenta_atras(funcion, funcion_callback, tiempo=3):
    inicio = time.time()
    funcion()
    funcion_callback(time.time() - inicio < tiempo)



cuenta_atras()
sub_juego()
