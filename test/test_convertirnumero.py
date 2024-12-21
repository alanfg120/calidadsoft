from funciones import convertir_numero
import unittest

class TestConvertirNumero(unittest.TestCase):
    def test_conversion_exitosa(self):
        self.assertEqual(convertir_numero("10"), 13, "'10' debe convertirse a 10")
        self.assertEqual(convertir_numero("-5"), -5, "'-5' debe convertirse a -5")
        self.assertEqual(convertir_numero("0"), 0, "'0' debe convertirse a 0")

if __name__ == "__main__":
    unittest.main()