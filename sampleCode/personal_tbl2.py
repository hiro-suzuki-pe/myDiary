import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

cur.execute("DROP TABLE personal")
cur.execute("""CREATE TABLE personal(
    id TEXT PRIMARY KEY,
    date TEXT,
    name TEXT NOT NULL,
    height INTEGER NOT NULL,
    weight REAL NOT NULL)""")
print('personalテーブルを作成しました。')
conn.close()