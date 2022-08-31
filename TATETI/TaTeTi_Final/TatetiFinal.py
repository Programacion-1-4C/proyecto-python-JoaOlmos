from menu_tateti import menu
from tateti import jugar as jugar1
from tateti_IA import jugar


menu()
elegir = int(input("Elija una de las opciones (1/2/3)\n>>>"))
if elegir == 1:
    jugar1()
elif elegir == 2:
    jugar()
