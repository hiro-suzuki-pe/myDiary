import sqlite3

conn = sqlite3.connect('sample.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE personal(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    height INTEGER NOT NULL,
    weight REAL NOT NULL)""")
conn.close()