import urllib.request

import cv2
import face_recognition
import numpy as np


def fetch_face_encoding(user_id: str, api_url_template: str):
    """Fetch remote face image and compute encoding."""
    url = api_url_template.format(user_id=user_id)

    with urllib.request.urlopen(url) as response:
        image_bytes = np.asarray(bytearray(response.read()), dtype="uint8")

    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("No se pudo decodificar la imagen de referencia desde la API.")

    face_locations = face_recognition.face_locations(image)
    if not face_locations:
        raise ValueError("La API no devolvio un rostro detectable.")

    face_encodings = face_recognition.face_encodings(image, known_face_locations=[face_locations[0]])
    if not face_encodings:
        raise ValueError("No se pudo generar el encoding facial de referencia.")

    return face_encodings[0]

