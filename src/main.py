"""Main entry point for the Gradio application.

Follows 12-factor principles:
1. All configuration comes from environment variables (.env loaded in development).
2. The application is self-contained and can be launched with `python -m app` or `python -m app.main`.
"""
from __future__ import annotations

from dotenv import load_dotenv
load_dotenv()

import ui

def main() -> None:
    """Launch the Gradio app."""
    demo = ui.create_interface()
    demo.launch(server_name="0.0.0.0", show_api=False, pwa=True)

if __name__ == "__main__":
    main()
    