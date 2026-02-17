import tkinter as tk

from ..atoms.frame import make_frame
from ..molecules.camera_panel import build_camera_panel
from ..molecules.header import build_header
from ..molecules.instruction_panel import build_instruction_panel


def build_main_layout(app):
    app.root = tk.Tk()
    app.root.title("Sistema de Reconocimiento")

    screen_width = app.root.winfo_screenwidth()
    screen_height = app.root.winfo_screenheight()
    window_width = int(screen_width * 0.9)
    window_height = int(screen_height * 0.8)
    x_pos = (screen_width - window_width) // 2
    y_pos = (screen_height - window_height) // 2

    app.root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
    app.root.configure(bg="#008b5f")

    app.root.grid_rowconfigure(0, weight=1)
    app.root.grid_columnconfigure(0, weight=1)
    app.root.grid_columnconfigure(1, weight=1)

    app.left_frame = make_frame(app.root, "#008b5f", row=0, column=0, sticky="nsew", padx=20, pady=20)
    app.left_frame.grid_rowconfigure(1, weight=1)
    app.left_frame.grid_columnconfigure(0, weight=1)

    app.right_frame = make_frame(app.root, "#008b5f", row=0, column=1, sticky="nsew", padx=20, pady=20)
    app.right_frame.grid_rowconfigure(0, weight=1)
    app.right_frame.grid_rowconfigure(1, weight=1)
    app.right_frame.grid_columnconfigure(0, weight=1)

    build_header(app, app.left_frame, "#008b5f")
    build_camera_panel(app, app.left_frame, "#008b5f")
    build_instruction_panel(app, app.right_frame, "#008b5f")
