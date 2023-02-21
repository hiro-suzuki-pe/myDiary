import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

for row in cur.execute("SELECT * FROM personal WHERE name LIKE 'Yamada Taro'"):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal WHERE name LIKE 'Tanaka%'"):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal WHERE name LIKE '%ro%'"):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal WHERE name LIKE '____ki%'"):
    print(row)
print('-')

for row in cur.execute("SELECT * FROM personal WHERE name LIKE '___________'"):
    print(row)
print('-')

conn.close()