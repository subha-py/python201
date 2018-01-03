import unittest
from .math import add

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_add_integers(self):
        result = add(1,2)
        self.assertEqual(result,2)

    def test_add_floats(self):
        result = add(10.5,2)
        self.assertEqual(result,12.5)

    def test_add_strings(self):
        result = add('abc','def')
        self.assertEqual('abcdef',result)

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAdd))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

if __name__ == '__main__':
    my_suite()

# to skip add @unitest.skip(condition,"reason to skip")