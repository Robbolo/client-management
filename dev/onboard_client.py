import tkinter as tk
import tkinter.ttk as ttk
from utils import *

def create_question(location, string, xpad=5, ypad=20):
    label = tk.Label(location,
                        text=string,
                        width=20,
                        height=2,
                        fg='indigo',
                        bg='lavender')
    label.pack(side='left', padx=xpad, pady=ypad)
    return label

def create_add_client_frame(window):
    title_frame = tk.Frame(window, bg='lavender')
    title_frame.pack(fill='both', expand=True)
    title = tk.Label(title_frame,
                     text='Add Client Details',
                     fg = 'indigo',
                     bg = 'lavender',
                     font=('Ariel', 38))
    title.pack(fill='both', expand=True, padx=50, pady=50)

    deets_frame = tk.Frame(window, bg='lavender')
    deets_frame.pack(fill='both', expand=True)

    left_frame = tk.Frame(deets_frame, bg='lavender')
    left_frame.pack(side='left', fill='both', expand=True)

    right_frame = tk.Frame(deets_frame, bg='lavender')
    right_frame.pack(side='right', fill='both', expand=True)

    q1 = tk.Frame(left_frame, bg='lavender')
    q1.pack(fill='both', expand=True, padx=5, pady=5)
    name = create_question(q1, 'Name:')
    name_entry = tk.Entry(q1,bg='white',highlightbackground='grey')
    name_entry.pack(side='right', padx=5, pady=5)