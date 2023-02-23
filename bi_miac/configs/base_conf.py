from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

CONF_DIR = BASE_DIR / "configs"
CONF_HEADER = CONF_DIR / "header.yaml"

TEMPLATES_DIR = BASE_DIR / "bi_cmd" / "templates"