import unittest
import Calculator


class MyTestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.addiction(10, 5), 15)
        self.assertEqual(Calculator.addiction(30, 20), 50)
        self.assertNotEqual(Calculator.addiction(30, 20), 0)
        self.assertNotEqual(Calculator.addiction(10, 5), 0)

    def test_sub(self):
        self.assertEqual(Calculator.subtractor(10, 5), 5)
        self.assertEqual(Calculator.subtractor(30, 20), 10)
        self.assertNotEqual(Calculator.subtractor(30, 20), 0)
        self.assertNotEqual(Calculator.subtractor(10, 5), 0)

    def test_mul(self):
        self.assertEqual(Calculator.multiple(10, 5), 50)
        self.assertEqual(Calculator.multiple(30, 20), 600)
        self.assertNotEqual(Calculator.multiple(30, 20), 0)
        self.assertNotEqual(Calculator.multiple(10, 5), 0)

    def test_div(self):
        self.assertEqual(Calculator.divisor(10, 5), 2)
        self.assertEqual(Calculator.divisor(30, 20), 1.5)
        self.assertNotEqual(Calculator.divisor(30, 20), 0)
        self.assertNotEqual(Calculator.divisor(10, 5), 0)


if __name__ == '__main__':
    unittest.main()
