def panel_de_juego():
    print("-------------------------")
    print("|-------|-------|-------|")
    print(f"|   {p7}   |   {p8}   |   {p9}   |")
    print("|-------|-------|-------|")
    print(f"|   {p4}   |   {p5}   |   {p6}   |")
    print("|-------|-------|-------|")
    print(f"|   {p1}   |   {p2}   |   {p3}   |")
    print("|-------|-------|-------|")
    print("-------------------------")

p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = " "
tabla = {p1:1, p2:2, p3:3, p4:4, p5:5, p6:6, p7:7, p8:8, p9:9}
TurnoJugador1 = True
Terminado = False
Ganador = False

panel_de_juego()
