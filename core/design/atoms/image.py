import tkinter as tk
from PIL import Image, ImageTk


def load_photo(path, size):
    image = Image.open(path)
    image = image.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)


def make_image_label(parent, image, bg, **kwargs):
    return tk.Label(parent, image=image, bg=bg, **kwargs)
