import tkinter as tk

master = tk.Tk()

def cmdButton():
  print("Button Push")

def cmdButtonArgs(arg):
  print("Button Push and {}".format(arg))

tk.Button(master, text="Button", command=cmdButton).pack()
tk.Button(master, text="Button", command=lambda : cmdButtonArgs("Arg")).pack()

master.mainloop()