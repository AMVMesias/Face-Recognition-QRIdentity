from ..atoms.frame import make_frame
from ..atoms.image import load_photo, make_image_label
from ..atoms.text import make_label


def build_header(app, parent, bg):
    app.header_frame = make_frame(parent, bg, row=0, column=0, pady=20, sticky="ew")
    app.header_frame.grid_rowconfigure(0, weight=1)
    app.header_frame.grid_rowconfigure(1, weight=1)
    app.header_frame.grid_columnconfigure(0, weight=1)

    app.welcome_label = make_label(
        app.header_frame,
        text="Bienvenido a QRIdentity",
        font=("Arial", 60, "bold"),
        bg=bg,
        fg="white",
    )
    app.welcome_label.grid(row=0, column=0, padx=(150, 0), sticky="w")

    try:
        app.logo_photo = load_photo(app.assets_dir / "logo.png", (120, 120))
        app.logo_label = make_image_label(app.root, app.logo_photo, bg)
        app.logo_label.place(relx=0.95, rely=0.02, anchor="ne")
        app.logo_label.lift()
    except Exception as e:
        print(f"Error cargando logo: {e}")
