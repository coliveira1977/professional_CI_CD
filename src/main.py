"""
Entry point for the Hello World application.

This module demonstrates a clean, professional structure:
- Separation of concerns (business logic vs. presentation)
- Type annotations and docstrings
- Use of the standard library only
"""

from __future__ import annotations

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
    argv : list[str] or None, optional
        Command‑line arguments. If omitted, ``sys.argv`` is used.

    Returns
    -------
    int
        Exit status (0 for success).
    """
    args = argv if argv is not None else sys.argv[1:]
    # Aqui você pode processar argumentos futuros com argparse,
    # mas para este exemplo simples apenas exibe a mensagem.
    message = get_greeting()
    print(message)
    return 0


if __name__ == "__main__":
    exit(main())