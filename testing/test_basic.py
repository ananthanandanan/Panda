import unittest
import basic

class TestBasic(unittest.TestCase):
    
    def test_add(self):
        
        self.assertEqual(basic.add(5,10),15)
        
    def test_sub(self):
        
        self.assertEqual(basic.sub(10,5),5)

    def test_multipy(self):
        
        self.assertEqual(basic.multiply(5,2),10)
    
    def test_divide(self):
        
        self.assertEqual(basic.division(4,2),2)
        
        with self.assertRaises(ValueError):
            basic.division(10,0)