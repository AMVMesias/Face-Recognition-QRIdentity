import tkinter as tk


def make_frame(parent, bg, row=None, column=None, **grid_kwargs):
    frame = tk.Frame(parent, bg=bg)
    if row is not None and column is not None:
        frame.grid(row=row, column=column, **grid_kwargs)
    return frame
