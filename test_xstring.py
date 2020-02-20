import unittest
import xstring

class MyTestxstring(unittest.TestCase):
    def test_add(self):
        self.assertEqual(xstring.add("5","6"), "56")
        self.assertEqual(xstring.add("1","2"), "12")
    def test_length(self):
        self.assertEqual(xstring.length("5"), 1)
        self.assertEqual(xstring.length("5555"), 4)
    def test_substr(self):
        s = "Hello"
        self.assertEqual(xstring.substr(s,2), "llo")
        self.assertNotEqual(xstring.substr(s,2), "lo")

if __name__ == '__main__':
    unittest.main()
