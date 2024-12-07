from funciones import devolver_none
import unittest

class TestDevolverNone(unittest.TestCase):
    def test_longitud_menor_o_igual_a_4(self):
        self.assertEqual(devolver_none("Hola"), "Hola", "Debe devolver 'Hola' si la longitud es menor o igual a 4")
        self.assertEqual(devolver_none("1234"), "Hola", "Debe devolver 'Hola' si la longitud es igual a 4")

    def test_longitud_mayor_a_4(self):
        self.assertIsNone(devolver_none("Holaaa"), "Debe devolver None si la longitud es mayor a 4")
        self.assertIsNone(devolver_none("12345"), "Debe devolver None si la longitud es mayor a 4")

if __name__ == "__main__":
    unittest.main()