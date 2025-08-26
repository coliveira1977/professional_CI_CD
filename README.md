# Hello World App

Um exemplo simples e profissional de aplicação Python que imprime “Hello, World!” com timestamp.

## Como executar

```bash
python -m src.main
```

ou, se você preferir instalar localmente:

```bash
pip install -e .
hello-world   # comando criado no pyproject.toml
```
```

---

#### 3️⃣ `pyproject.toml` (opcional, mas recomendado)

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "hello-world-app"
version = "0.1.0"
description = "Um Hello World profissional em Python."
authors = [{ name="Seu Nome", email="seu@email.com" }]
readme = "README.md"
requires-python = ">=3.8"

[tool.setuptools.packages.find]
where = ["src"]

[project.scripts]
hello-world = "src.main:main"
```

---

#### 4️⃣ `tests/test_hello.py`

```python
import unittest
from src.hello import get_greeting

class TestHello(unittest.TestCase):
    def test_get_greeting(self):
        msg = get_greeting()
        self.assertTrue(msg.startswith("Hello, World! – "))
        # verifica se há um espaço depois do hífen e que o timestamp está presente
        parts = msg.split("–")
        self.assertEqual(len(parts), 2)
        self.assertTrue(len(parts[1].strip()) > 0)

if __name__ == "__main__":
    unittest.main()
```

---

### Como criar esses arquivos rapidamente

```bash
mkdir -p hello_world_app/src hello_world_app/tests
touch hello_world_app/.gitignore hello_world_app/README.md hello_world_app/pyproject.toml
touch hello_world_app/src/__init__.py hello_world_app/src/main.py hello_world_app/src/hello.py
touch hello_world_app/tests/__init__.py hello_world_app/tests/test_hello.py