import cv2
from PIL import Image, ImageTk

from .design.organisms.main_layout import build_main_layout


def build_interface(app):
    build_main_layout(app)


def render_camera_frame(app, frame):
    if frame is None:
        return

    container_width = app.camera_container.winfo_width()
    container_height = app.camera_container.winfo_height()
    if container_width <= 1 or container_height <= 1:
        return

    base_size = min(container_width, container_height)
    target_size = int(base_size * app.camera_frame_scale)

    height, width = frame.shape[:2]
    min_dim = min(width, height)
    start_x = (width - min_dim) // 2
    start_y = (height - min_dim) // 2
    frame = frame[start_y : start_y + min_dim, start_x : start_x + min_dim]
    frame = cv2.resize(frame, (target_size, target_size))

    qr_size = int(target_size * app.qr_frame_scale)
    qr_offset = (target_size - qr_size) // 2
    app.qr_frame = {
        "x": qr_offset,
        "y": qr_offset,
        "width": qr_size,
        "height": qr_size,
    }

    if not app.face_data:
        cv2.rectangle(
            frame,
            (app.qr_frame["x"], app.qr_frame["y"]),
            (
                app.qr_frame["x"] + app.qr_frame["width"],
                app.qr_frame["y"] + app.qr_frame["height"],
            ),
            (0, 255, 0),
            2,
        )

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame)
    photo = ImageTk.PhotoImage(image=image)
    app.camera_frame.configure(image=photo)
    app.camera_frame.image = photo
