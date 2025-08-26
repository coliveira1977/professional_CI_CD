# tests/test_hello.py
import unittest
from src.hello import get_greeting

class TestHello(unittest.TestCase):
    """Testes para a função `get_greeting`."""

    def test_get_greeting(self):
        """
        Deve retornar uma string no formato:
            "Hello, World! – <timestamp>"
        Onde <timestamp> é o horário UTC atual.
        """
        msg = get_greeting()
        # 1. Verifica prefixo
        self.assertTrue(msg.startswith("Hello, World! – "))
        # 2. Separa em partes e garante que há um timestamp não vazio
        parts = msg.split("–")
        self.assertEqual(len(parts), 2)
        self.assertTrue(len(parts[1].strip()) > 0)

if __name__ == "__main__":
    unittest.main()