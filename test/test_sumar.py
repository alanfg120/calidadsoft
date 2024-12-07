
from funciones import sumar
import unittest




class TestSumar(unittest.TestCase):
    
    def test_1(self):
        resultado = sumar(3,4,7)
        self.assertEqual(resultado,14)
      

  

if __name__ == '__main__':
    unittest.main()