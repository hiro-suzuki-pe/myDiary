import sqlite3

conn = sqlite3.connect('diary.db')
cur = conn.cursor()

for row in cur.execute("SELECT * FROM diary"):
    print(row)

conn.close()