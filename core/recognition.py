import face_recognition
from pyzbar.pyzbar import decode


def read_qr_user_id(frame):
    for qr in decode(frame):
        qr_data = qr.data.decode("utf-8")
        data_parts = qr_data.split("-")
        if len(data_parts) >= 5:
            user_id = data_parts[4].strip()
            if user_id:
                return user_id
    return None


def iter_face_matches(frame, known_encoding):
    face_locations = face_recognition.face_locations(frame)
    for face_location in face_locations:
        encodings = face_recognition.face_encodings(frame, [face_location])
        if not encodings:
            continue
        is_match = face_recognition.compare_faces([known_encoding], encodings[0])[0]
        yield is_match, face_location
