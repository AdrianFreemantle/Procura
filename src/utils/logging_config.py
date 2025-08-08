import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path

try:
  from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover
  load_dotenv = None  # type: ignore

_INITIALIZED = False

def init_logging() -> None:
  """Initialize application-wide file-based logging.
  Reads configuration from environment variables (optionally via .env):
  - LOG_LEVEL (default: INFO)
  - LOG_FILE (default: logs/procura.log)
  - LOG_MAX_BYTES (default: 1048576)
  - LOG_BACKUP_COUNT (default: 5)
  - LOG_FORMAT (default: "%(asctime)s %(levelname)s %(name)s - %(message)s")
  - LOG_DATE_FORMAT (default: "%Y-%m-%d %H:%M:%S")
  Safe to call multiple times; only configures once.
  """
  global _INITIALIZED
  if _INITIALIZED:
    return

  # Load .env if python-dotenv is available
  if load_dotenv:
    try:
      load_dotenv()
    except Exception:
      pass

  level_name = os.getenv("LOG_LEVEL", "INFO").upper()
  log_file = os.getenv("LOG_FILE", "logs/procura.log")
  max_bytes = int(os.getenv("LOG_MAX_BYTES", "1048576"))
  backup_count = int(os.getenv("LOG_BACKUP_COUNT", "5"))
  fmt = os.getenv("LOG_FORMAT", "%(asctime)s %(levelname)s %(name)s - %(message)s")
  datefmt = os.getenv("LOG_DATE_FORMAT", "%Y-%m-%d %H:%M:%S")

  # Ensure log directory exists
  log_path = Path(log_file)
  try:
    log_path.parent.mkdir(parents=True, exist_ok=True)
  except Exception:
    # Fallback to current directory if path is invalid
    log_file = "procura.log"
    log_path = Path(log_file)

  # Configure root logger if not already configured
  root = logging.getLogger()
  if not root.handlers:
    root.setLevel(getattr(logging, level_name, logging.INFO))
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8")
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    handler.setFormatter(formatter)
    root.addHandler(handler)
  else:
    # Adjust level if env overrides
    root.setLevel(getattr(logging, level_name, logging.INFO))

  _INITIALIZED = True
