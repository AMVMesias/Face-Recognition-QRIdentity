import cv2

from .api_client import fetch_face_encoding
from .config import ACCESS_LOG_FILE, IMG_DIR, load_api_url_template
from .logger import AccessLogger
from .ui import build_interface, render_camera_frame
from .workflows.camera import process_camera_frame
from .workflows.security import (
    reset_recognition_timer as reset_recognition_timer_action,
    show_lock_screen as show_lock_screen_action,
    show_success_screen as show_success_screen_action,
    start_recognition_timer as start_recognition_timer_action,
    unlock_system as unlock_system_action,
)


class SistemaReconocimiento:
    def __init__(self):
        self.assets_dir = IMG_DIR
        self.logger = AccessLogger(ACCESS_LOG_FILE)
        self.api_url_template = load_api_url_template()

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise ValueError("No se pudo abrir la camara")

        self.cam_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.cam_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.is_scanning = False
        self.face_data = None
        self.last_frame = None
        self.qr_frame = {"x": 0, "y": 0, "width": 0, "height": 0}
        self.camera_frame_scale = 0.8
        self.qr_frame_scale = 0.8
        self.locked = False
        self.recognition_start_time = None

        build_interface(self)
        self.root.bind("<Configure>", self.on_window_resize)

        self.is_scanning = True
        self.update_camera()

    def log_attempt(self, user_id, status, detail):
        self.logger.log_attempt(user_id, status, detail)

    def on_window_resize(self, event):
        if event.widget == self.root and self.last_frame is not None:
            render_camera_frame(self, self.last_frame)

    def update_camera(self):
        if self.is_scanning and not self.locked:
            ret, frame = self.cap.read()
            if ret:
                process_camera_frame(self, frame)
                render_camera_frame(self, self.last_frame)

            self.root.after(10, self.update_camera)

    def start_face_recognition(self, desired_data):
        self.user_id = desired_data
        self.face_image_encodings = fetch_face_encoding(desired_data, self.api_url_template)
        self.log_attempt(self.user_id, "API_OK", f"Usuario {self.user_id} identificado")
        self.status_label.config(text="Realizando reconocimiento facial...")

    def show_success_screen(self):
        show_success_screen_action(self)

    def run(self):
        self.root.mainloop()

    def __del__(self):
        if hasattr(self, "cap") and self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()

    def start_recognition_timer(self):
        start_recognition_timer_action(self)

    def reset_recognition_timer(self):
        reset_recognition_timer_action(self)

    def show_lock_screen(self):
        show_lock_screen_action(self)

    def unlock_system(self):
        unlock_system_action(self)


def run():
    app = SistemaReconocimiento()
    app.run()
