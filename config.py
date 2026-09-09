from typing import Final

# Konfigurace barev
COLORS: Final[dict[str, str]] = {
    "primary": "#0B132B",
    "accent": "#7F2982",
    "error": "#F7717D",
    "background": "#D8D6E6",
    "text": "#0B132B",
}

# Konstanty pro nastavení aplikace
WINDOW_TITLE: Final[str] = "PyQt Calculator"
DEFAULT_PRECISION: Final[int] = 5
NUMBER_RANGE_MIN: Final[int] = -10000000
NUMBER_RANGE_MAX: Final[int] = 10000000
INITIAL_RESULT: Final[str] = "0.0"
MAX_HISTORY_SIZE: Final[int] = 10 * 1024 * 1024  # 10MB limit
