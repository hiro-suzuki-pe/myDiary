import sqlite3
import tkinter as tk
from tkinter import messagebox

def save():
    con = sqlite3.connect('diary.db', isolation_level=None,)
    cur = con.cursor()
    r_data = ['2022_1_1', 2, 80, 4, """あけまして、おめでとう。
目が覚めたら10時だった。
今年こそは、ダイエットすると決めていたのに、
結局だらだら1日が過ぎてしまった。"""]
    sql = "REPLACE INTO diary VALUES (?,?,?,?,?)"
    cur.execute(sql, r_data)
    con.commit()
    con.close()
    messagebox.showinfo('メッセージ', '"2022_1_1のデータを保存しました。')
    
    
def delete():
    con = sqlite3.connect('diary.db')
    cur = con.cursor()
    sql = "DELETE FROM diary WHERE date='2022_1_1';"
    cur.execute(sql)
    con.commit()
    con.close()
    messagebox.showinfo('メッセージ', '"2022_1_1のデータを削除しました。')
    
def search():

#    messagebox.showinfo('メッセージ', '検索メニューです。')
    global s_txt
    global s_text
    
    sub_window = tk.Toplevel()
    sub_window.geometry('320x220')
    sub_window.title('検索テスト')
 
    s_txt = tk.Entry(sub_window, width=20)
    s_txt.pack(pady=10)
    
    button = tk.Button(sub_window, text='検索', command=click_search)
    button.pack()
    
    frame = tk.Frame(sub_window)
    s_text = tk.Text(frame, width=40, height=10)
    s_text.grid(row=0, column=0)
    scroll_v = tk.Scrollbar(frame, orient=tk.VERTICAL, command=s_text.yview)
    scroll_v.grid(row=0, column=1, sticky=tk.N+tk.S)
    s_text["yscrollcommand"] = scroll_v.set
    frame.pack(pady=10)
    
def click_search():
    global s_txt
    global s_text
    
    con = sqlite3.connect('diary.db')
    cur = con.cursor()
    sql = """SELECT * FROM diary WHERE event LIKE '%""" \
        + s_txt.get() + """%' ORDER BY date DESC;"""
    cur.execute(sql)
    s_text.delete('1.0', 'end')
    for row in cur:
        s_text.insert('1.0', row[0] + '\n' + row[4] + '\n\n')
    con.close()
        
        
        
root=tk.Tk()
root.geometry('320x220')
root.title('メニューテスト')

men = tk.Menu(root)
root.config(menu=men)

menu_command = tk.Menu(root)
men.add_cascade(label='操作', menu=menu_command)

menu_command.add_command(label='保存', command=save)
menu_command.add_separator()
menu_command.add_command(label='削除', command=delete)
menu_command.add_separator()
menu_command.add_command(label='検索', command=search)

root.mainloop()

