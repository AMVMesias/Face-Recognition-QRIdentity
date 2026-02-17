from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = APP_DIR.parent
IMG_DIR = APP_DIR / "img"
CONFIG_DIR = APP_DIR / "config"
API_URL_FILE = CONFIG_DIR / "api_url.txt"
API_URL_EXAMPLE_FILE = CONFIG_DIR / "api_url.example.txt"
ACCESS_LOG_FILE = PROJECT_DIR / "access_log.csv"


def load_api_url_template() -> str:
    """Load API URL template from config file."""
    if not API_URL_FILE.exists():
        raise FileNotFoundError(
            f"No se encontro {API_URL_FILE}. Crea el archivo desde {API_URL_EXAMPLE_FILE}."
        )

    template = API_URL_FILE.read_text(encoding="utf-8").strip()
    if not template:
        raise ValueError(f"{API_URL_FILE} esta vacio.")
    if "{user_id}" not in template:
        raise ValueError("La URL de API debe incluir el placeholder {user_id}.")

    return template
