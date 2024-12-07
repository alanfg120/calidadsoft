from funciones import dividir
import unittest

class TestDividir(unittest.TestCase):
    def test_division_correcta(self):
        self.assertEqual(dividir(10, 2), 5, "10 dividido por 2 debe ser 5")
        self.assertEqual(dividir(-10, 2), -5, "-10 dividido por 2 debe ser -5")
        self.assertAlmostEqual(dividir(1, 3), 0.3333, places=4, msg="1 dividido por 3 debe aproximarse a 0.3333")

    def test_division_por_uno(self):
        self.assertEqual(dividir(5, 1), 5, "5 dividido por 1 debe ser 5")

    def test_division_por_menos_uno(self):
        self.assertEqual(dividir(5, -1), -5, "5 dividido por -1 debe ser -5")

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError, msg="Dividir entre cero debe generar un ZeroDivisionError"):
            dividir(10, 0)

if __name__ == "__main__":
    unittest.main()