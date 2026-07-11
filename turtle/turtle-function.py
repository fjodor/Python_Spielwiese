# Funktion spielerisch erforschen mit turtle

from turtle import *

# Dreieck zeichnen
# Winkel: 360 Grad / Anzahl Ecken = 360 / 3 = 120

# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)
# left(120)

# Damit das Zeichenfenster offen bleibt
# mainloop()

# Eleganter: n-Ecke per Funktion

def n_eck(n):
    winkel = (360 / n)

    for i in range(n):
        forward(100)
        left(winkel)

    mainloop()

# Beispielaufruf

# n_eck(3)

# Sechseck

n_eck(6)