import tkinter as tk


def start_recognition_timer(app):
    app.recognition_start_time = app.root.after(20000, app.show_lock_screen)


def reset_recognition_timer(app):
    if app.recognition_start_time:
        app.root.after_cancel(app.recognition_start_time)
        app.recognition_start_time = None


def show_success_screen(app):
    app.log_attempt(app.user_id, "ACCESO_COMPLETADO", f"Usuario {app.user_id} accedio correctamente")

    for widget in app.root.winfo_children():
        widget.destroy()

    app.root.configure(bg="#008b5f")
    success_label = tk.Label(
        app.root,
        text="PUEDE PASAR",
        font=("Arial", 120, "bold"),
        bg="#008b5f",
        fg="white",
    )
    success_label.place(relx=0.5, rely=0.5, anchor="center")
    app.root.after(3000, app.root.destroy)


def show_lock_screen(app):
    if app.face_data:
        app.log_attempt(app.face_data, "TIMEOUT", "Tiempo de reconocimiento excedido")
    else:
        app.log_attempt("DESCONOCIDO", "TIMEOUT", "Tiempo de escaneo QR excedido")

    app.locked = True
    app.is_scanning = False
    reset_recognition_timer(app)

    for widget in app.root.winfo_children():
        widget.destroy()

    app.root.configure(bg="#ff0000")
    lock_message = tk.Label(
        app.root,
        text="SISTEMA BLOQUEADO\nReintente en 3 minutos",
        font=("Arial", 60, "bold"),
        bg="#ff0000",
        fg="white",
    )
    lock_message.place(relx=0.5, rely=0.5, anchor="center")
    app.root.after(7000, app.root.destroy)


def unlock_system(app):
    app.locked = False
    app.face_data = None
    app.root.destroy()
    app.__init__()
    app.run()
