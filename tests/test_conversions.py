'''
BANTUAN AI 🤖
'''

import unittest
from src.conversions import Celcius, Fahrenheit, Reamur, Rankine, Kelvin

class TestTemperatureConversions(unittest.TestCase):

    def test_celcius(self):
        self.assertEqual(Celcius(0), (0, 32.0, 273.15, 0.0, 491.67))
        
    def test_fahrenheit(self):
        self.assertEqual(Fahrenheit(32), (32, 0, 273.15, 0.0, 491.67))
        
    def test_reamur(self):
        self.assertEqual(Reamur(0), (0, 0.0, 32.0, 273.15, 491.67))
        
    def test_rankine(self):
        self.assertEqual(Rankine(491.67), (491.67, 0, 32, 273.15, 0.0))
        
    def test_kelvin(self):
        self.assertEqual(Kelvin(273.15), (273.15, 0, 32, 0.0, 491.67))

if __name__ == '__main__':
    unittest.main()
