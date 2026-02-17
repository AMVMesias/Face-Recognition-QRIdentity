# Face Recognition QRIdentity

Aplicativo de control de acceso que combina validacion por QR y reconocimiento facial en una interfaz de escritorio con `tkinter`.

## Que hace

- Escanea un codigo QR desde camara.
- Extrae `user_id` del QR.
- Consulta imagen de referencia en una API privada.
- Compara rostro en tiempo real contra el rostro de referencia.
- Registra eventos en CSV (`QR_OK`, `API_OK`, `ACCESO_OK`, `ACCESO_DENEGADO`, `TIMEOUT`).

## Estructura del proyecto

```text
apps/
  main.py
  requirements.txt
  img/
    logo.png
    qr_instruction.png
    face_instruction.png
    images.ico
  config/
    api_url.example.txt
    api_url.txt          # NO versionado (privado)
  core/
    app.py               # orquestador principal
    api_client.py        # consulta API + encoding facial
    recognition.py       # lectura QR + comparacion de rostros
    logger.py            # escritura de logs CSV
    config.py            # rutas y carga de configuracion
    ui.py                # render de camara
    design/              # Atomic Design (UI)
      atoms/
      molecules/
      organisms/
    workflows/           # flujos de negocio
      camera.py
      security.py
```

## Requisitos

- Python 3.11 o superior recomendado.
- Camara funcional.
- Dependencias en `apps/requirements.txt`.

## Instalacion (Windows / PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r apps/requirements.txt
```

## Configuracion de API privada

1. Copia el template:

```powershell
Copy-Item .\apps\config\api_url.example.txt .\apps\config\api_url.txt
```

2. Edita `apps/config/api_url.txt` con tu URL privada real.

Formato esperado:

```text
https://YOUR_PRIVATE_API_HOST/endpoint/{user_id}
```

`{user_id}` es obligatorio.

## Ejecucion

```powershell
python .\apps\main.py
```

## Seguridad y confidencialidad

- `apps/config/api_url.txt` esta ignorado por git.
- No subas credenciales, endpoints reales ni tokens.
- Mantener solo placeholders en archivos versionados.

## Logs

- Archivo principal: `access_log.csv` (raiz del proyecto).
- Sandbox: `access_log_sandbox.csv`.

## Notas

- Si la app no inicia, verifica que la camara no este ocupada por otra aplicacion.
- Si falla la API, valida `apps/config/api_url.txt` y conectividad de red.
