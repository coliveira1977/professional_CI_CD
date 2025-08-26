```python src/main.py
"""
Ponto de entrada para a aplicação Hello World.

Este módulo demonstra uma estrutura limpa e profissional:
- Separação de preocupações (lógica de negócio vs. apresentação)
- Anotações de tipo e docstrings
- Uso da biblioteca padrão apenas
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
    Executa a aplicação.

    Parameters
    ----------
    argv : list[str] | None, optional
        Argumentos de linha de comando. Se omitido, ``sys.argv`` é usado.

    Returns
    -------
    int
        Status de saída (0 para sucesso).
    """
    parser = argparse.ArgumentParser(description="Imprime uma mensagem de saudação.")
    parser.add_argument("--name", type=str, help="O nome para incluir na mensagem de saudação.", default="Mundo")
    args = parser.parse_args(argv)

    message = get_greeting(name=args.name)
    print(message)
    return 0


if __name__ == "__main__":
    exit(main())
