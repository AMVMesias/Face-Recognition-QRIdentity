# Face-Recognition-QRIdentity

Aplicacion de control de acceso que combina validacion por codigo QR y reconocimiento facial en una interfaz de escritorio con `tkinter`.

Repositorio: `https://github.com/AMVMesias/Face-Recognition-QRIdentity`

## Que hace

- Escanea un codigo QR desde camara.
- Extrae `user_id` del QR.
- Consulta la imagen de referencia en una API privada.
- Compara el rostro en tiempo real contra el rostro de referencia.
- Registra eventos en CSV (`QR_OK`, `API_OK`, `ACCESO_OK`, `ACCESO_DENEGADO`, `TIMEOUT`).

## Estructura del proyecto

```text
.
├── main.py
├── requirements.txt
├── README.md
├── img/
│   ├── logo.png
│   ├── qr_instruction.png
│   ├── face_instruction.png
│   └── images.ico
├── config/
│   ├── api_url.example.txt
│   └── api_url.txt          # NO versionado (privado)
└── core/
    ├── app.py
    ├── api_client.py
    ├── recognition.py
    ├── logger.py
    ├── config.py
    ├── ui.py
    ├── design/
    │   ├── atoms/
    │   ├── molecules/
    │   └── organisms/
    └── workflows/
        ├── camera.py
        └── security.py
```

## Requisitos

- Python 3.11 o superior recomendado.
- Camara funcional.
- Dependencias en `requirements.txt`.

## Instalacion (Windows / PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\requirements.txt
```

## Configuracion de API privada

1. Copia el template:

```powershell
Copy-Item .\config\api_url.example.txt .\config\api_url.txt
```

2. Edita `config/api_url.txt` con tu URL privada real.

Formato esperado:

```text
https://YOUR_PRIVATE_API_HOST/endpoint/{user_id}
```

`{user_id}` es obligatorio.

## Ejecucion

```powershell
python .\main.py
```

## Seguridad y confidencialidad

- `config/api_url.txt` esta ignorado por git.
- No subas credenciales, endpoints reales ni tokens.
- Mantener solo placeholders en archivos versionados.

## Logs

- Archivo principal: `../access_log.csv` (por implementacion actual).

## Notas

- Si la app no inicia, verifica que la camara no este ocupada por otra aplicacion.
- Si falla la API, valida `config/api_url.txt` y conectividad de red.
