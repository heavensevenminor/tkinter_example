import tkinter as tk
from pathlib import Path

master = tk.Tk()

master.title('Tkinter for band')

master.geometry("300x400+10+20")


screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

master.resizable(True, True)

master.minsize(100, 100)
master.maxsize(screen_width//2,screen_height//2)

master.attributes('-alpha', 1)
master.attributes('-topmost', True)

# 같은 폴더에 있는 아이콘 불러 오기
master.iconbitmap(default=Path(__file__).with_name('favicon.ico'))

# 작업표시줄에 아이콘 변경
try:
  from ctypes import windll  # Only exists on Windows.
  windll.shell32.SetCurrentProcessExplicitAppUserModelID("mycompany.myproduct.subproduct.version")
except ImportError:
  pass

master.mainloop()