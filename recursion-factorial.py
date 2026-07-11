# Quelle: Python lernen kurz und gut - Michael Inden
# S. 214

def fac(n):
    if n == 0:
        return 1
    print("Rufe fac(" + str(n - 1) + ")")
    return n * fac(n-1)

# Beispielaufruf
print(fac(5))
