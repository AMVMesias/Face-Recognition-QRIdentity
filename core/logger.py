import csv
from datetime import datetime
from pathlib import Path


class AccessLogger:
    def __init__(self, log_file: Path):
        self.log_file = Path(log_file)
        self._initialize()

    def _initialize(self) -> None:
        if not self.log_file.exists():
            with self.log_file.open("w", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Fecha", "Hora", "Usuario", "Estado", "Detalle"])

    def _next_id(self) -> int:
        try:
            with self.log_file.open("r", encoding="utf-8-sig") as file:
                return len(list(csv.reader(file)))
        except Exception:
            return 1

    def log_attempt(self, user_id: str, status: str, detail: str) -> None:
        now = datetime.now()
        next_id = self._next_id()

        with self.log_file.open("a", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    next_id,
                    now.strftime("%Y-%m-%d"),
                    now.strftime("%H:%M:%S"),
                    user_id,
                    status,
                    detail,
                ]
            )

