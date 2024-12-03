import random
import string
import unittest
from app.scripts.charfun import esPalindromo

def generar_texto_aleatorio():
    """Genera una cadena aleatoria con longitud entre 10 y 40, incluyendo mayúsculas, minúsculas, números y símbolos."""
    longitud = random.randint(10, 40)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(caracteres, k=longitud))

def generar_palindromo_aleatorio():
    """Genera un palíndromo aleatorio con longitud entre 10 y 40, incluyendo mayúsculas, minúsculas, números y símbolos."""
    mitad = generar_texto_aleatorio()[:random.randint(5, 20)]
    return mitad + mitad[::-1]

class TestEsPalindromo(unittest.TestCase):

    def test_generar_texto_aleatorio_no_palindromo(self):
        """Testea que la función generar_texto_aleatorio no genere palíndromos."""
        for _ in range(100):  # Realiza múltiples intentos para verificar la aleatoriedad.
            texto = generar_texto_aleatorio()
            self.assertFalse(esPalindromo(texto))

    def test_generar_palindromo_aleatorio(self):
        """Testea que la función generar_palindromo_aleatorio siempre genere palíndromos."""
        for _ in range(100):  # Repite múltiples veces para garantizar consistencia.
            palindromo = generar_palindromo_aleatorio()
            self.assertTrue(esPalindromo(palindromo))

    def test_palindromos_simples(self):
        """Testea cadenas que son palíndromos simples."""
        for palabra in ["ana", "otto", "radar"]:
            self.assertTrue(esPalindromo(palabra))

    def test_palindromos_complejos(self):
        """Testea cadenas con mayúsculas, espacios y tildes."""
        for palabra in ["Anita lava la tina","Átale, demoníaco Caín o me delata"]:
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
