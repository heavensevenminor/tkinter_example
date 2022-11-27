# import tkinter as tk

# master = tk.Tk()

# master.mainloop()

import pyautogui
import time
time.sleep(3)
window_title = pyautogui.getActiveWindowTitle()
print(window_title)