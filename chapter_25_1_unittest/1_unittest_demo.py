from .math import add
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_add_integers(self):
        result = add(1,1)
        self.assertEqual(result,3)

    def test_add_floats(self):
        result = add(10.5,2)
        self.assertEqual(result,12.5)

    def test_add_strings(self):
        result = add('abc','def')
        self.assertEqual('abcdef',result)

if __name__ == '__main__':
    unittest.main()