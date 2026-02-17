from ..atoms.frame import make_frame
from ..atoms.text import make_label


def build_camera_panel(app, parent, bg):
    app.camera_container = make_frame(parent, bg, row=1, column=0, sticky="nsew")
    app.camera_container.grid_rowconfigure(0, weight=1)
    app.camera_container.grid_columnconfigure(0, weight=1)

    app.camera_frame = make_label(
        app.camera_container,
        text="",
        font=("Arial", 12),
        bg=bg,
        fg="white",
    )
    app.camera_frame.grid(row=0, column=0)

    app.message_label = make_label(
        parent,
        text="",
        font=("Arial", 24, "bold"),
        bg=bg,
        fg="white",
    )
    app.message_label.grid(row=2, column=0, pady=20)
