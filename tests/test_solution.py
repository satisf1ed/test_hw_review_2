"""Trusted instructor tests for reviewflow-synthetic-courses-v1, HW 4."""
import unittest
import solution


class Requirements(unittest.TestCase):
    def test_ascii_and_empty(self):
        self.assertEqual(solution.budget_context(["cat", "dog"], 20), "cat\ndog")
        self.assertEqual(solution.budget_context([], 0), "")
        self.assertEqual(solution.budget_context(["cat"], 0), "")

    def test_invalid_budget(self):
        for budget in [-1, True]:
            with self.subTest(budget=budget), self.assertRaises(ValueError):
                solution.budget_context(["cat"], budget)

    def test_separators(self):
        self.assertEqual(solution.budget_context(["abc", "de"], 5), "abc")
        self.assertEqual(solution.budget_context(["abc", "de"], 6), "abc\nde")

    def test_utf8_bytes(self):
        self.assertEqual(solution.budget_context(["\u00e9"], 1), "")
        self.assertEqual(solution.budget_context(["\u00e9"], 2), "\u00e9")

    def test_prefix_not_greedy_skip(self):
        self.assertEqual(solution.budget_context(["a", "oversized", "b"], 3), "a")


if __name__ == "__main__":
    unittest.main()
