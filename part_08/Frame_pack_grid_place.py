import tkinter as tk

master = tk.Tk()

frm_pack = tk.Frame(master, bg='#FAA')
frm_grid = tk.Frame(master, bg='#AFA')
frm_place = tk.Frame(master, bg='#AAF')

frm_pack.pack(fill=tk.BOTH, expand=True)
frm_grid.pack(fill=tk.BOTH, expand=True)
frm_place.pack(fill=tk.BOTH, expand=True)

tk.Button(frm_pack, text="LEFT").pack(side=tk.LEFT)
tk.Button(frm_pack, text="LEFT").pack(side=tk.LEFT)
tk.Button(frm_pack, text="TOP").pack(side=tk.TOP)
tk.Button(frm_pack, text="TOP").pack(side=tk.TOP)
tk.Button(frm_pack, text="RIGHT").pack(side=tk.RIGHT)
tk.Button(frm_pack, text="RIGHT").pack(side=tk.RIGHT)
tk.Button(frm_pack, text="BOTTOM").pack(side=tk.BOTTOM)
tk.Button(frm_pack, text="BOTTOM").pack(side=tk.BOTTOM)

tk.Button(frm_grid, text="GRID").grid(row=0, column=0)
tk.Button(frm_grid, text="GRID").grid(row=1, column=0)
tk.Button(frm_grid, text="GRID").grid(row=2, column=0)
tk.Button(frm_grid, text="GRID").grid(row=3, column=0)
tk.Button(frm_grid, text="GRID").grid(row=4, column=0)
tk.Button(frm_grid, text="GRID").grid(row=5, column=0)
tk.Button(frm_grid, text="GRID").grid(row=5, column=1)
tk.Button(frm_grid, text="GRID").grid(row=5, column=2)
tk.Button(frm_grid, text="GRID").grid(row=5, column=3)
tk.Button(frm_grid, text="GRID").grid(row=5, column=4)
tk.Button(frm_grid, text="GRID").grid(row=5, column=5)

tk.Button(frm_place, text="PLACE").place(x=10, y=10)
tk.Button(frm_place, text="PLACE").place(x=30, y=50)
tk.Button(frm_place, text="PLACE").place(relx=0.5, rely=0.2)

master.geometry("300x900+0+0")
master.mainloop()