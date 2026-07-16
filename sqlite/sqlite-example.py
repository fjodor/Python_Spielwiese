import sqlite3

conn = sqlite3.connect("example.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("INSERT INTO users(name) VALUES('Wolf')")
conn.commit()

for row in cur.execute("SELECT * FROM users"):
    print(row)