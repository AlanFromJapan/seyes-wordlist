import unittest
from seyes_wordlist import generate_page
import seyes_maths

class TestSeyesWordlist(unittest.TestCase):

    def setUp(self):
        pass

    # def test_generate_page(self):
    #     # Test if generate_page returns a PIL Image
    #     generate_page(
    #         ["il y a", "un jardin", "quatre", "du chocolat", "un garçon", "alors", "après", "je m'appelle", "les vacances"], 
    #         path_to_save="test01.png"
    #     )

    #     generate_page(
    #         [], 
    #         path_to_save="test02.png"
    #     )

    #     generate_page(
    #         ["AAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAA", "bbbbbbbbbbbbbbb", "hhhhhhhhhhhhhhhhh", "qqqqqqqqqqqqq", "ggggggggggg"], 
    #         path_to_save="test03.png"
    #     )
        

    def test_math_addition(self):
        # Test if math_addition returns a string
        result = seyes_maths.math_addition()
        print(result)
        self.assertIsInstance(result, str)
        self.assertIn("+", result)
        self.assertIn("=", result)

    def test_math_substraction(self):
        # Test if math_substraction returns a string
        result = seyes_maths.math_substraction()
        print(result)
        self.assertIsInstance(result, str)
        self.assertIn("-", result)
        self.assertIn("=", result)

    def test_math_multiplication(self):
        # Test if math_multiplication returns a string
        result = seyes_maths.math_multiplication(max_number=5)
        print(result)
        self.assertIsInstance(result, str)
        self.assertIn("×", result)
        self.assertIn("=", result)

    def test_math_division(self):
        # Test if math_division returns a string
        result = seyes_maths.math_division(max_number=5)
        print(result)
        self.assertIsInstance(result, str)
        self.assertIn("/", result)
        self.assertIn("=", result)

if __name__ == '__main__':
    unittest.main()