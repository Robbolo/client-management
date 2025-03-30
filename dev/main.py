import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from utils import *
from start_page import *


window = tk.Tk()
window.configure(bg='lavender')
create_start_page()
window.mainloop()