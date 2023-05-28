
import unittest

class TestStringMethods(unittest.TestCase):
    def testtask(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def testtask2(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def testtask3(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

# Run the test as follows:
# python abctest.py -v

# Output:
# test_isupper (__main__.TestStringMethods) ... ok
# test_split (__main__.TestStringMethods) ... ok
# test_upper (__main__.TestStringMethods) ... ok
