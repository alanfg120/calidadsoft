from funciones import mayor_edad
import unittest




class TestMayorEdad(unittest.TestCase):
    
    def test_1(self):
        resultado = mayor_edad(20)
        self.assertEqual(resultado, 1)

if __name__ == '__main__':
    unittest.main()