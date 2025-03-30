import tkinter as tk
from utils import *

def create_start_page():

    start_page_frame = tk.Frame(window, bg = 'lavender')
    start_page_frame.pack()

    top_frame = tk.Frame(start_page_frame, bg='lavender')
    top_frame.pack(fill='both', expand=True)

    title = create_header_label(top_frame,
                    string='Katie\'s Client & User Management')


    mid_frame = tk.Frame(start_page_frame, bg='lavender')
    mid_frame.pack(fill='both', expand=True)

    img_frame = tk.Frame(mid_frame, bg='lavender')
    img_frame.pack(side='left', fill='both',expand=True)

    add_image_label(img_frame, 'dev/butterfly.png')

    btn_frame = tk.Frame(mid_frame, bg='lavender')
    btn_frame.pack(side='left', fill='both', expand=True)

    todo_btn = create_button(btn_frame, 'See to-do list')
    view_btn = create_button(btn_frame, 'View clients')
    add_btn = create_button(btn_frame, 'Add new client')


    right_img = tk.Frame(mid_frame, bg='lavender')
    right_img.pack(side='right', fill='both', expand=True)

    add_image_label(right_img, 'dev/flutter.png')

    quote_frame = tk.Frame(start_page_frame, bg='lavender',highlightthickness=4, highlightbackground="#76199B")
    quote_frame.pack(padx=50, pady=50)
    quote_label = create_quote_label(quote_frame)
