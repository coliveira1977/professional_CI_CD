"""
Module that encapsulates the greeting logic.

Keeping this in its own module makes it trivial to test,
extend, or replace without touching the application entry point.
"""

from datetime import datetime

def get_greeting() -> str:
    """
    Return a professional “Hello World” message with a timestamp.

    Returns
    -------
    str
        A greeting string that includes the current UTC time.
    """
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"Hello, World! – {now}"