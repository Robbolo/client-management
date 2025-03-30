import tkinter as tk
from utils import *
from start_page import *
from onboard_client import *


window = tk.Tk()
window.configure(bg='lavender')
window.geometry('1200x800')

create_start_page(window)

window.mainloop()