import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

for row in cur.execute("SELECT * FROM personal ORDER BY height"):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal ORDER BY id DESC"):
    print(row)
print('-')

conn.close()