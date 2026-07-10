# Wie viele Versuche maximal, um per binärer Suche einen Wert zu finden?
# Erinnerung: Liste muss bereits sortiert sein

import math

Listenlänge = int(input("Wie viele Werte enthält Deine sortierte Liste? "))

Suchschritte = math.ceil(math.log2(Listenlänge))

print(f"Du brauchst maximal {Suchschritte} Suchschritte.")

