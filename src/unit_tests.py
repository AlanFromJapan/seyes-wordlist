import unittest
from seyes_wordlist import generate_page

class TestSeyesWordlist(unittest.TestCase):

    def setUp(self):
        pass

    def test_generate_page(self):
        # Test if generate_page returns a PIL Image
        generate_page(
            ["il y a", "un jardin", "quatre", "du chocolat", "un garçon", "alors", "après", "je m'appelle", "les vacances"], 
            path_to_save="test01.png"
        )

        generate_page(
            [], 
            path_to_save="test02.png"
        )

        generate_page(
            ["AAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAA", "bbbbbbbbbbbbbbb", "hhhhhhhhhhhhhhhhh", "qqqqqqqqqqqqq", "ggggggggggg"], 
            path_to_save="test03.png"
        )
        


if __name__ == '__main__':
    unittest.main()