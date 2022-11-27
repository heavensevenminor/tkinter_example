import tkinter as tk

master = tk.Tk()

tk.Label(master, text="This is label.", font=("Helvetica", 20)).pack()
tk.Label(master, text="This is small label.", font=("Times", 15)).pack()
tk.Label(master, text="This is other.", font=("MS Sans Serif", 20)).pack()

tk.Button(master, text="normal").pack()
tk.Button(master, text="Button", font=("Terminal", 20)).pack()
tk.Button(master, text="Padding", padx=10, pady=10).pack()

strId = tk.StringVar(value="initial value")
strId.set("initial value set")
tk.Entry(master, textvariable=strId).pack()

strId.get()

ent = tk.Entry(master)
ent.get()

pw = tk.StringVar()
tk.Entry(master, textvariable=pw, show="*").pack()

master.mainloop()