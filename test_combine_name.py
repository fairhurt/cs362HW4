import unittest

from combine_name import combine_first_and_last

class TestAverage(unittest.TestCase):
    def test1 (self):
        self.assertEqual(combine_first_and_last('John', 'Smith'), 'John Smith')
    def test2 (self):
        self.assertEqual(combine_first_and_last('John', 1),'Last name is not a string')
    def test3 (self):
        self.assertEqual(combine_first_and_last(3, "Smith"), 'First name is not a string')
    
        
  
if __name__ == '__main__':
    unittest.main(verbosity=2)
        
        
