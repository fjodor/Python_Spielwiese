# albums2000-Daten

# 1. Daten verstehen

# Ein Album kann mehrfach in den Charts auftauchen.
# Redundanz vermeiden: 1:n, zwei Tabellen: Album, ChartEntry

# 2. csv einlesen

import pandas as pd
df = pd.read_csv("albums2000.csv")

# Alternative
# import csv
# with open("albums2000.csv", newline = "", encoding = "utf-8") as f:
#   reader = csv.DictReader(f)
#   rows = list(reader)

# 3. Daten bereinigen

# 4. SQLite-Datenbank anlegen

# 5. Tabellen erstellen

# 6. Daten einfügen

# 7. SQL direkt in PyCharm ausführen

