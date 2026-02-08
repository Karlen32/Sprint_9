import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
BASE_URL = (
    os.environ.get("BASE_URL", "https://foodgram-frontend-1.prakticum-team.ru")
    or "https://foodgram-frontend-1.prakticum-team.ru"
).rstrip("/")
SELENOID_URL = os.environ.get("SELENOID_URI")
DEFAULT_TIMEOUT = int(os.environ.get("DEFAULT_TIMEOUT", 10))