# coding: utf-8
import os
import sqlite3

if not os.path.exists('diary.db'):
    print('diary.dbを作成します。')
con = sqlite3.connect('diary.db')
cur = con.cursor()

try:
    cur.execute("DROP TABLE dialy")
except:
    pass
cur.execute("""CREATE TABLE dialy(date TEXT PRIMARY KEY,
            weather INTEGER,
            adequacy INTEGER,
            action INTEGER,
            event TEXT)""")
print('dialyテーブルを作成しました。')

sql = """INSERT INTO dialy
(date, weather, adequacy, action, event)
VALUES('2022_1_1', 2, 80, 4, 'あけまして、おめでとう。
目が覚めたら10時だった。
今年こそは、ダイエットすると決めていたのに、
結局だらだら1日が過ぎてしまった。')"""
try:
    cur.execute(sql)
except EOFError as e:
    print('Error: ', e)
print(cur)
print('1月1日データを登録しました。')

sql = """INSERT INTO dialy
(date, weather, adequacy, action, event)
VALUES('2022_1_3', 1, 40, 4, '今日は7時に起きて、久々に街へ出かけた。
駅前は、結構にぎわっている。
このまま、コロナが終息するといいなぁ。')"""
cur.execute(sql)
print('1月3日データを登録しました。')


sql = """INSERT INTO dialy
(date, weather, adequacy, action, event)
VALUES('2022_1_4', 3, 60, 1, 
'やっぱり寝坊したけど、ズーム会議は13時からなので余裕。
今日、やっとジムに行くことができた。
マジで痩せないと。今年の目標は10k減。')"""
cur.execute(sql)
print('1月4日データを登録しました。', cur)

for row in cur.execute("SELECT * FROM dialy"):
    print(str(row[0]) + "," + str(row[1]) + "," + str(row[2])
          + "," + str(row[3]) + "," + str(row[4]))
          
con.commit()
con.close()