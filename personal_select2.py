import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

for row in cur.execute("SELECT * FROM personal WHERE id = '002'"):
    print(row)
print()

for row in cur.execute("SELECT * FROM personal WHERE height >= 173"):
    print(row)
print()

for row in cur.execute("SELECT * FROM personal WHERE weight != 75.8"):
    print(row)
print()


conn.close()