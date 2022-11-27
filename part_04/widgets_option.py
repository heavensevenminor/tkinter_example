import tkinter as tk
from tkinter import ttk

master =  tk.Tk()

def cmdButton():
  print("Button Push")
  
tk.Button(master, text="Button", command=cmdButton).pack()

btn = tk.Button(master, text="Button_variable")
btn.pack()
btn["command"] = cmdButton

strEnt = tk.StringVar()
strEnt.set("Entry_StringVar")

tk.Entry(master, textvariable=strEnt).pack()

ent = tk.Entry(master)
ent.pack()
ent.insert(tk.END, "Entry_variable")

tk.Checkbutton(master, text="Checkbutton").pack()
tk.Label(master, text="Label").pack()
tk.Radiobutton(master, text="Radiobutton").pack()
tk.Canvas(master, bg='#fff', width=100, height=100).pack()
tk.Scale(master).pack()
tk.Scrollbar(master).pack()
mnb = tk.Menubutton(master, text="Menubutton", relief = tk.RAISED)
men = tk.Menu(mnb, tearoff = 0)
men.add_checkbutton(label="Menu")
mnb["menu"] = men
mnb.pack()

lsb = tk.Listbox(master, height=3)
lsb.insert(1,"Listbox")
lsb.pack()

master.mainloop()