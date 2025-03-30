import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import pandas as pd
import random
from onboard_client import *
from pathlib import Path


def create_button(location, string, command_fn, xpad=30, ypad=10):
    button = tk.Button(location,
                        text=string,
                        width=20,
                        height=2,
                        fg='indigo',
                        bg='lavender',
                        command = command_fn)
    button.pack(padx=xpad, pady=ypad)

def process_image_for_background(image_path, bg):
    image = Image.open(image_path).convert('RGBA')
    background = Image.new('RGBA', image.size, bg)
    background.paste(image,(0,0), image)
    return background.convert('RGB')

def add_image_label(frame_location, image_path):
    processed_image = process_image_for_background(image_path, (230,230,250))
    tk_image = ImageTk.PhotoImage(processed_image)
    img_label = tk.Label(frame_location, image=tk_image, bg='lavender')
    img_label.image = tk_image
    img_label.pack()

def create_header_label(location, string):
    label = tk.Label(location,
                     text=string,
                     fg = 'indigo',
                     bg = 'lavender',
                     font=('Ariel', 38))
    label.pack(fill='both', expand=True, padx=50, pady=50)

def create_question(location, string, xpad=5, ypad=20):
    label = tk.Label(location,
                        text=string,
                        width=20,
                        height=2,
                        fg='indigo',
                        bg='lavender')
    label.pack(padx=xpad, pady=ypad)

def load_quote(): 
    script_dir = Path(__file__).parent
    print(script_dir)
    quotes_path = script_dir / 'quotes.csv'
    quotes = pd.read_csv(quotes_path)
    random_loc = random.randint(0, len(quotes) - 1)
    quote = quotes['Quote'].iloc[random_loc]
    return quote


def create_quote_label(location, width=50, height=6):
    label = tk.Label(location,
                     text=load_quote(),
                     fg = 'indigo',
                     bg = 'lavender',
                     font=('Ariel', 25),
                     wraplength = 600,
                     justify = 'center'
                     )
    label.pack(padx=50, pady=50, anchor='center')
    return None

def clear_window(new_page, window):
    for widget in window.winfo_children():
        widget.destroy()
    new_page()

def move_to_add_client(window):
    for widget in window.winfo_children():
        widget.destroy()
        create_add_client_frame(window)

