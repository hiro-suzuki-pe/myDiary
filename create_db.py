import sqlite3

conn = sqlite3.connect('sample.db')
print('データベースを作成しました。')

conn.close()
