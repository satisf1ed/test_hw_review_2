"""Trusted instructor tests for reviewflow-synthetic-courses-v1, HW 1."""
import unittest
import solution


class Requirements(unittest.TestCase):
    def test_punctuation_and_duplicates(self):
        self.assertEqual(solution.tokenize("cat,dog! cat"), ["cat", "dog", "cat"])

    def test_empty(self):
        self.assertEqual(solution.tokenize(""), [])
        self.assertEqual(solution.tokenize(" -- ! "), [])

    def test_casefold(self):
        self.assertEqual(solution.tokenize("Cat DOG"), ["cat", "dog"])

    def test_digits(self):
        self.assertEqual(solution.tokenize("gpt4 has 32 layers"), ["gpt4", "has", "32", "layers"])

    def test_stopwords(self):
        self.assertEqual(solution.tokenize("the cat and dog", ["THE", "and"]), ["cat", "dog"])


if __name__ == "__main__":
    unittest.main()
