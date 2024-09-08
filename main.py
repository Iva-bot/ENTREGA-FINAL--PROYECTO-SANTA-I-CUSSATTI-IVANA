#prueba unitaria
import unittest

def suma(a , b):
    return  a + b

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        resultado= suma(3 , 5)
        self.assertEqual(resultado, 8)

if __name__=='__main__':
    unittest.main()       

#prueba ad-hoc

from datetime import datetime as dt

def return_today(self):
        day= dt.now()
        return day.day
   

def return_year(self):
        year= dt.now()
        return 2060

hoy = dt.now()
assert return_today() == hoy.day

assert return_year() == hoy.year

print("¡Todas las pruebas pasaron exitosamente!")