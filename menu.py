import sqlite3
import tkinter as tk
from tkinter import messagebox

def save():
    messagebox.showinfo('メッセージ', '保存メニューです。')
    
def delete():
    messagebox.showinfo('メッセージ', '削除メニューです。')
    
def search():
    messagebox.showinfo('メッセージ', '検索メニューです。')
    
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

