from menu_tateti import menu
elegir = int(input("Elija una de las opciones (1/2)\n>>>"))
if elegir == 1:
    from tateti import jugar, ver_tablero, tablero
elif elegir == 2:
    import random
    from tateti_IA import jugar, ver_tablero, tablero
    jugar()