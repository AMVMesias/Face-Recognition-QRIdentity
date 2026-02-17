import tkinter as tk


def make_label(parent, text, font, bg, fg="white", **kwargs):
    return tk.Label(parent, text=text, font=font, bg=bg, fg=fg, **kwargs)
