"""Trusted instructor tests for reviewflow-synthetic-courses-v1, HW 3."""
import unittest
import solution


class Requirements(unittest.TestCase):
    def test_ranked_hits(self):
        self.assertEqual(solution.retrieval_metrics(["x", "a", "b"], {"a", "b"}, 3), {"recall": 1.0, "mrr": 0.5})

    def test_no_relevant_or_no_hits(self):
        self.assertEqual(solution.retrieval_metrics(["a"], set(), 2), {"recall": 0.0, "mrr": 0.0})
        self.assertEqual(solution.retrieval_metrics([], {"a"}, 2), {"recall": 0.0, "mrr": 0.0})

    def test_cutoff(self):
        self.assertEqual(solution.retrieval_metrics(["x", "a"], {"a"}, 1), {"recall": 0.0, "mrr": 0.0})

    def test_duplicates(self):
        self.assertEqual(solution.retrieval_metrics(["a", "a"], {"a", "b"}, 2), {"recall": 0.5, "mrr": 1.0})

    def test_invalid_k(self):
        for k in [0, -1, True]:
            with self.subTest(k=k), self.assertRaises(ValueError):
                solution.retrieval_metrics(["a"], {"a"}, k)


if __name__ == "__main__":
    unittest.main()
