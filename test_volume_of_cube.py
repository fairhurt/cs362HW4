import unittest

from volume_of_cube import volume_cube

class TestVolume(unittest.TestCase):
    def test1(self):
        correct= 5
        self.assertEqual(volume_cube(correct), 125)
   
    def test2(self):
        negative = -5
        self.assertEqual(volume_cube(negative),'Value must be greater than zero')
    
    def test3(self):
        noninteger= 'xyz'
        self.assertEqual(volume_cube(noninteger),'Not a proper input. Please input a integer')

if __name__ == '__main__':
    unittest.main(verbosity=2)
        
        