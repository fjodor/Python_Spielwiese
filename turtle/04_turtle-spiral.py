# Quelle: https://docs.python.org/3/library/turtle.html#making-algorithmic-patterns

# from turtle import *
# Das ist zwar bequem, aber problematisch, z. B. wegen der Gefahr von Namenskonfliken
# In Skripten ist das Folgende besser:

import turtle as t

# Dann muss der Namensraum (namespace) immer angegeben werden; hier: t.forward() statt nur forward()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(30)

t.mainloop()