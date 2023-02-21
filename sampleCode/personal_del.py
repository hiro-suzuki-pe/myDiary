import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

cur.execute("DROP TABLE personal")

conn.close()