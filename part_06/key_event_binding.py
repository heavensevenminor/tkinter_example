import tkinter as tk

master = tk.Tk()

def bidBtn(event):
  print("Button Push")

def bidBtnWithout():
  print("Button Push")

btn = tk.Button(master, text="Button")
btn.bind('<Return>', bidBtn)
btn.pack()

btn.focus()

ent = tk.Entry(master)
ent.bind('<Return>', lambda e: print('Entry'))
ent.pack()

master.mainloop()