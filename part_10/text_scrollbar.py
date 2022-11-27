import tkinter as tk
from tkinter.scrolledtext import ScrolledText
# import sqlite3

# con = sqlite3.connect(":memory")
# cur = con.cursor()

# cur.execute("CREATE TABLE text(index INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)")
# cur.execute("INSERT INTO test(text) VALUES ('sample')")

master = tk.Tk()

sct = ScrolledText(master, width=20,  height=10)
sct.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

for i in range(20):
  sct.insert(tk.END,'ScrolledText\n')

master.mainloop()