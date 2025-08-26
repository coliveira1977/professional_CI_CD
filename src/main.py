"""
Entry point for the Hello World application.

This module demonstrates a clean, professional structure:
- Separation of concerns (business logic vs. presentation)
- Type annotations and docstrings
- Use of the standard library only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Importa a função que gera a mensagem de saudação.
# A lógica fica em hello.py para manter o código organizado.
from src.hello import get_greeting


def main(argv: list[str] | None = None) -> int:
    """
    Execute the application.

    Parameters
    ----------
    argv : list[str] | None, optional
        Command‑line arguments. If omitted, ``sys.argv`` is used.

    Returns
    -------
    int
        Exit status (0 for success).
    """
    parser = argparse.ArgumentParser(description="Prints a greeting message.")
    parser.add_argument("--name", type=str, help="The name to include in the greeting message.", default="World")
    args = parser.parse_args(argv)

    message = get_greeting(name=args.name)
    print(message)
    return 0


if __name__ == "__main__":
    exit(main())
