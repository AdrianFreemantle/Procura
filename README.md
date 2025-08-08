# Procura

Lightweight interview/chat manager with thread-safe SQLite persistence and a Gradio UI.

## Features
- Thread-safe in-memory SQLite store (`check_same_thread=False` + lock)
- Integer `context_id` with `context_status` ("empty", "active", "archived")
- `ChatManager` persistence via `SqlLiteContextStore`
- Gradio UI: create/switch chats, sidebar listing, status refresh after first send
- File-based logging configured via `.env`

## Requirements
- Python 3.10+ (3.10–3.12 recommended)

## Quickstart
```bash
# 1) Create a virtual environment
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Optional: configure logging
copy .env.example .env  # then edit values as needed

# 4) Run the app
python src/main.py
```

The UI will start a Gradio app. By default, it launches with a new blank chat.

## Configuration
Configuration is via environment variables. See `.env.example` for defaults:
- `LOG_LEVEL` (e.g., `INFO`)
- `LOG_FILE` (e.g., `logs/procura.log`)
- `LOG_MAX_BYTES` (e.g., `1MB`)
- `LOG_BACKUP_COUNT` (e.g., `5`)
- `LOG_FORMAT`, `LOG_DATE_FORMAT`

Logging is initialized in `src/utils/logging_config.py`.

## Testing
```bash
pip install -r requirements.txt
pytest -q
```
Integration tests use an in-memory SQLite DB and stub external calls. A dummy `OPENAI_API_KEY` is set within tests to avoid client initialization errors.

## Project structure
```
src/
  agents/
    chat_manager.py
    context_management/
      persistence/sqlite_store.py
  ui.py
  main.py
tests/
  test_chat_manager_integration.py
  test_sqlite_store_integration.py
```

## License
MIT — see `LICENSE`.
