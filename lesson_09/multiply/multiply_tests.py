import unittest
from multiply import multiply_3_numbers

class Testing(unittest.TestCase):
    def test_1(self):
        result = multiply_3_numbers(5, 5, 5)
        self.assertEqual(result, 125)

    def test_2(self):
        result = multiply_3_numbers(5,5,5)
        self.assertNotEqual(result, 100)

    def test_3(self):
        result = multiply_3_numbers(-5, -5, 5)
        self.assertTrue(result > 0)

    def test_4(self):
        result = multiply_3_numbers(-5, -5, -5)
        self.assertFalse(result > 0)

    def test_5(self):
        num_list = [5, 125, 100, 58]
        result = multiply_3_numbers(5, 5, 5)
        self.assertIn(result, num_list)

if __name__ == "__main__":
    unittest.main()