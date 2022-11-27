import tkinter as tk
from tkinter import ttk

master =  tk.Tk()

ntb = ttk.Notebook(master)
ntb.pack()

frm_tk = ttk.Frame(ntb)
frm_tk.pack()
frm_ttk = ttk.Frame(ntb)
frm_ttk.pack()

# FRAME tk
ntb.add(frm_tk, text="tk widget")
ntb.add(frm_ttk, text="ttk widget")

strEnt = tk.StringVar()
strEnt.set('Entry')

tk.Button(frm_tk, text="Button").pack()
tk.Checkbutton(frm_tk, text="Checkbutton").pack()
tk.Entry(frm_tk, textvariable=strEnt).pack()
tk.Label(frm_tk, text="Label").pack()
tk.Radiobutton(frm_tk, text="Radiobutton").pack()
tk.Canvas(frm_tk, bg='#fff', width=100, height=100).pack()
tk.Scale(frm_tk).pack()
tk.Scrollbar(frm_tk).pack()
mnb = tk.Menubutton(frm_tk, text="Menubutton", relief = tk.RAISED)
men = tk.Menu(mnb, tearoff = 0)
men.add_checkbutton(label="Menu")
mnb["menu"] = men
mnb.pack()

lsb = tk.Listbox(frm_tk, height=3)
lsb.insert(1,"Listbox")
lsb.pack()

# FRAME ttk
strSpb = tk.StringVar()
strSpb.set('Spinbox')

strCbb = tk.StringVar()
strCbb.set('Combobox')

ttk.Button(frm_ttk, text="Button").pack()
ttk.Checkbutton(frm_ttk, text="Checkbutton").pack()
ttk.Entry(frm_ttk, textvariable=strEnt).pack()
ttk.Label(frm_ttk, text="Label").pack()
ttk.Radiobutton(frm_ttk, text="Radiobutton").pack()
ttk.Scale(frm_ttk).pack()
ttk.Scrollbar(frm_ttk).pack()
ttk.Spinbox(frm_ttk, textvariable=strSpb).pack()
ttk.Combobox(frm_ttk, textvariable=strCbb).pack()
ttk.Progressbar(frm_ttk, orient=tk.VERTICAL, mode='indeterminate', length=100).pack()
mnb = ttk.Menubutton(frm_ttk, text="Menubutton")
men = tk.Menu(mnb, tearoff = 0)
men.add_checkbutton(label="Menu")
mnb["menu"] = men
mnb.pack()

master.mainloop()