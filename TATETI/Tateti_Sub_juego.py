import time
from random import choice
contador = 3
contenido = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890!#$%&=?¿"
def sub_juego():
    print("Empezamos Jugador 1")
    while True:
        while True:
            print("Jugador 1, escriba el siguiente simbolo o letra, en menos de 3 segundos")
            aux = (choice(contenido))
            print(aux)
            ls = input()  # letra_simbolo
            for i in contenido:
                if ls == i and ls == aux:
                    print("Bien, Acertaste!")
                    break
            if ls == i:
                break
            elif ls != i:
                print("Fallaste")
                break
        if ls == i:
            confirmarJ1 = True
            break
        while True:
            print("Jugador 2, escriba el siguiente simbolo o letra, en menos de 3 segundos")
            aux = (choice(contenido))
            print(aux)
            ls = input()  # letra_simbolo
            for i in contenido:
                if ls == i and ls == aux:
                    print("Bien, Acertaste!")
                    break
            if ls == i:
                break
            elif ls != i:
                print("Fallaste")
                break
        if ls == i:
            break
def cuenta_atras(contador):
    while contador != 0:
        contador = contador - 1
        time.sleep(1)

sub_juego()
cuenta_atras(contador)