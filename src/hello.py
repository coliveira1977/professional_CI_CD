"""
Módulo que encapsula a lógica de saudação.

Manter isso em seu próprio módulo torna trivial testar,
extender ou substituir sem tocar no ponto de entrada do aplicativo.
"""

from datetime import datetime, timezone


def get_greeting(name: str | None = None) -> str:
    """
    Retorna uma mensagem profissional de “Hello World” com um timestamp.

    Parameters
    ----------
    name : str, optional
        O nome a ser incluído na saudação.

    Returns
    -------
    str
        Uma string de saudação que inclui a hora UTC atual.
    """
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    if name:
        return f"Hello, {name}! – {now}"
    return f"Hello, Mundo! – {now}"
