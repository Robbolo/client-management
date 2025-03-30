import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from utils import *


def create_button(location, string, xpad=30, ypad=10):
    button = tk.Button(location,
                        text=string,
                        width=20,
                        height=2,
                        fg='indigo',
                        bg='lavender')
    button.pack(padx=xpad, pady=ypad)

def process_image_for_background(image_path, bg):
    image = Image.open(image_path).convert('RGBA')
    background = Image.new('RGBA', image.size, bg)
    background.paste(image,(0,0), image)
    return background.convert('RGB')


window = tk.Tk()
window.configure(bg='lavender')

start_page_frame = tk.Frame(window, bg = 'lavender')
start_page_frame.pack()

top_frame = tk.Frame(start_page_frame, bg='lavender')
top_frame.pack(fill='both', expand=True)

title = tk.Label(top_frame,
                 text='Katie\'s Client & User Management',
                 font=('Ariel',25),
                 foreground = 'indigo',
                 background='lavender',
                 width=50,
                 height=6
                 )
title.pack()


bottom_frame = tk.Frame(start_page_frame, bg='lavender')
bottom_frame.pack(fill='both', expand=True)


btn_frame = tk.Frame(bottom_frame, bg='lavender')
btn_frame.pack(side='right', fill='both', expand=True)

todo_btn = create_button(btn_frame, 'See to-do list')
view_btn = create_button(btn_frame, 'View clients')
add_btn = create_button(btn_frame, 'Add new client')

img_frame = tk.Frame(bottom_frame, bg='lavender')
img_frame.pack(side='left', fill='both',expand=True)

try:
    processed_image = process_image_for_background('dev/butterfly.png', (230,230,250))
    tk_image = ImageTk.PhotoImage(processed_image)

    img_label = tk.Label(img_frame, image=tk_image, bg='lavender')
    img_label.image = tk_image
    img_label.pack()
except Exception as e: 
    print(f"Error loading image: {e}")


window.mainloop()