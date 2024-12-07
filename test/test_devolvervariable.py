from funciones import devolver_variable
import unittest




class TestDevolverVariable(unittest.TestCase):
    
    def test_1(self):
        resultado = devolver_variable(2)
        self.assertEqual(resultado, 2)

if __name__ == '__main__':
    unittest.main()