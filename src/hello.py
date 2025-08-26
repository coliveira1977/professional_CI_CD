```python src/hello.py
"""
Module that encapsulates the greeting logic.

Keeping this in its own module makes it trivial to test,
extend, or replace without touching the application entry point.
"""

from datetime import datetime, timezone

def get_greeting(name: str | None = None) -> str:
    """
    Return a professional “Hello World” message with a timestamp.

    Parameters
    ----------
    name : str, optional
        The name to include in the greeting.

    Returns
    -------
    str
        A greeting string that includes the current UTC time.
    """
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    if name:
        return f"Hello, {name}! – {now}"
    return f"Hello, World! – {now}"
```
