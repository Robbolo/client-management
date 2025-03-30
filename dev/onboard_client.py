import tkinter as tk
import tkinter.ttk as ttk


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