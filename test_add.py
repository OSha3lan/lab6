import unittest
from addition import addition

class TestAdd(unittest.TestCase):  
    def test_add(self):
        result = add.add(1, 1)
        self.assertEqual(result, 2)  
        result = add.add(-1, -2)
        self.assertEqual(result, -3)  

if __name__ == '__main__':
    unittest.main()
