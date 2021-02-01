import unittest

from average_elements import average_elements_list

class TestAverage(unittest.TestCase):
    def test1 (self):
        self.assertEqual(average_elements_list([5, 10, 15, 20]), 12.5)
    def test2 (self):
        self.assertEqual(average_elements_list([]), 'List cannot be empty divide by zero error')
    def test3 (self):
        self.assertEqual(average_elements_list([0,0,0,'fdg']), 'Must be integer')
    
        
  
if __name__ == '__main__':
    unittest.main(verbosity=2)
        
        