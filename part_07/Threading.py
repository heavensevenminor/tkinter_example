import tkinter as tk
import threading

master = tk.Tk()

def threadLong():
  result = 0
  for i in range(100000000):
    result += i
  txtLong.insert(tk.END, result)

tk.Button(master, text="Button", command=lambda : threading.Thread(target=threadLong).start()).pack()
txtLong = tk.Text(master, width=30, height=5)
txtLong.pack()

def threadShort():
  txtShort.insert(tk.END, 1+1)

tk.Button(master, text="Button", command=lambda : threading.Thread(target=threadShort).start()).pack()
txtShort = tk.Text(master, width=30, height=5)
txtShort.pack()

def threadArgs(input):
  txtArgs.insert(tk.END, int(input)*2)

tk.Button(master, text="Button", command=lambda : threading.Thread(target=threadArgs, args=(txtShort.get(0.0,tk.END),)).start()).pack()
txtArgs = tk.Text(master, width=30, height=5)
txtArgs.pack()

master.mainloop()