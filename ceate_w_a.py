# coding: utf-8
import os
import sqlite3

if not os.path.exists('diary.db'):
    print('diary.dbを作成します。')
con = sqlite3.connect('diary.db')
cur = con.cursor()

try:
    cur.execute("DROP TABLE weather")
except:
    pass
cur.execute("""CREATE TABLE weather
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT)""")
print('weatherテーブルを作成しました。')

weather = ['快晴', '晴れ', '曇り', '雨', '雪', '台風',
           '晴れのち曇り', '晴れのち雨', '晴れのち雪', '曇りのち晴れ',
           '曇りのち雨', '曇りのち雪', '雨のち晴れ', '雨のち曇り', '雨のち雪']

for w in weather:
    cur.execute("INSERT INTO weather(type) VALUES ('" + w + "')")
    

for row in cur.execute("SELECT * FROM weather"): 
    print(str(row[0]) + "," + str(row[1]))

try:
    cur.execute("DROP TABLE action")
except:
    pass
cur.execute("""CREATE TABLE action
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT)""")
print('actionテーブルを作成しました。')

action = ['出社', 'テレワーク', '外回り', '出張', '休日']

for a in action:
    cur.execute("INSERT INTO action(type) VALUES ('" + a + "')")
    

for row in cur.execute("SELECT * FROM action"): 
    print(str(row[0]) + "," + str(row[1]))

con.commit()
con.close()