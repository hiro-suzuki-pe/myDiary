import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

for row in cur.execute("SELECT * FROM personal WHERE height BETWEEN 170 AND 180"):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal WHERE height IN(160, 170, 180) "):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal WHERE height NOT IN(160, 170, 180) "):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal WHERE id IS NULL"):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal WHERE id IS NOT NULL"):
    print(row)
print('-')

conn.close()