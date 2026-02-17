import cv2

from ..recognition import iter_face_matches, read_qr_user_id


def process_camera_frame(app, frame):
    app.last_frame = frame.copy()

    if not app.face_data:
        _handle_qr_stage(app, frame)
        return

    if hasattr(app, "face_image_encodings"):
        _handle_face_stage(app, frame)


def _handle_qr_stage(app, frame):
    if not app.recognition_start_time:
        app.start_recognition_timer()

    user_id = read_qr_user_id(frame)
    if not user_id:
        return

    app.user_id = user_id
    app.log_attempt(app.user_id, "QR_OK", f"QR de usuario {app.user_id} validado")
    app.face_data = app.user_id
    app.reset_recognition_timer()
    app.message_label.config(text="QR VALIDADO")
    app.root.after(2000, lambda: app.message_label.config(text="Iniciando reconocimiento facial..."))
    app.instructions.config(text="Muestra tu rostro\nen frente de la camara")
    app.instruction_image.configure(image=app.face_photo)
    app.instruction_image.image = app.face_photo
    app.start_face_recognition(app.user_id)
    app.start_recognition_timer()


def _handle_face_stage(app, frame):
    for is_match, face_location in iter_face_matches(frame, app.face_image_encodings):
        if is_match:
            app.log_attempt(app.face_data, "ACCESO_OK", "Reconocimiento facial exitoso")
            app.reset_recognition_timer()
            app.message_label.config(text="ROSTRO VALIDADO")
            color = (124, 220, 0)
            app.root.after(1000, app.show_success_screen)
        else:
            app.log_attempt(app.face_data, "ACCESO_DENEGADO", "Rostro no coincide")
            app.message_label.config(text="ROSTRO NO VALIDADO")
            color = (50, 50, 255)

        cv2.rectangle(
            frame,
            (face_location[3], face_location[0]),
            (face_location[1], face_location[2]),
            color,
            2,
        )
        app.last_frame = frame.copy()
