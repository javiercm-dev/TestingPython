import unittest
from app.scripts.charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):

    def test_palindromos_simples(self):
        """Testea cadenas que son palíndromos simples."""
        for palabra in ["ana", "otto", "radar"]:
            self.assertTrue(esPalindromo(palabra))

    def test_palindromos_complejos(self):
        """Testea cadenas con mayúsculas, espacios y tildes."""
        for palabra in [
            "Anita lava la tina", 
            "Átale, demoníaco Caín o me delata"
        ]:
            self.assertTrue(esPalindromo(palabra))

    def test_no_palindromos(self):
        """Testea cadenas que no son palíndromos."""
        no_palindromos = [("caracola", False), ("esternocleidomastoideo", False), ("suzuki", False)]
        for palabra, esperado in no_palindromos:
            self.assertEqual(esPalindromo(palabra), esperado)

    def test_caracteres_especiales(self):
        """Testea cadenas con caracteres especiales."""
        self.assertEqual(esPalindromo("12422322421"), True)
        self.assertEqual(esPalindromo("!@#@$!$@#@!"), True)
        self.assertEqual(esPalindromo("1230392759823745"), False)

    def test_cadenas_vacias(self):
        """Testea el comportamiento con cadenas vacías."""
        self.assertEqual(esPalindromo(""), True)

    def test_uso_incorrecto(self):
        """Testea el comportamiento con entradas no válidas."""
        with self.assertRaises(TypeError):
            esPalindromo(None)
        with self.assertRaises(TypeError):
            esPalindromo(12345)

if __name__ == "__main__":
    unittest.main()
