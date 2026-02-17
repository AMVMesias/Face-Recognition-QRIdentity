import tkinter as tk

from ..atoms.image import load_photo, make_image_label
from ..atoms.text import make_label


def build_instruction_panel(app, parent, bg):
    app.instructions = make_label(
        parent,
        text="Muestra tu QR\nen frente de la camara",
        font=("Arial", 24, "bold"),
        bg=bg,
        fg="white",
        justify=tk.CENTER,
    )
    app.instructions.grid(row=0, column=0, pady=(0, 400), sticky="s")

    app.status_label = make_label(
        parent,
        text="Esperando QR...",
        font=("Arial", 14),
        bg=bg,
        fg="white",
    )
    app.status_label.grid(row=1, column=0, pady=0, sticky="n")

    app.qr_photo = _load_instruction_image(app.assets_dir, "qr_instruction.png", (400, 400))
    app.face_photo = _load_instruction_image(app.assets_dir, "face_instruction.png", (600, 400))

    app.instruction_image = make_image_label(parent, app.qr_photo, bg)
    app.instruction_image.place(relx=0.5, rely=0.6, anchor="center")


def _load_instruction_image(assets_dir, filename, size):
    try:
        return load_photo(assets_dir / filename, size)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None
