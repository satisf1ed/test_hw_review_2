"""Trusted instructor tests for reviewflow-synthetic-courses-v1, HW 2."""
import unittest
import solution


class Requirements(unittest.TestCase):
    def test_training_and_purity(self):
        rows = [{"id": 1, "group": "a"}]
        before = [dict(row) for row in rows]
        self.assertEqual(solution.split_by_group(rows, set()), (rows, []))
        self.assertEqual(rows, before)

    def test_empty(self):
        self.assertEqual(solution.split_by_group([], {"b"}), ([], []))

    def test_heldout_groups(self):
        rows = [{"id": 1, "group": "a"}, {"id": 2, "group": "b"}, {"id": 3, "group": "b"}]
        self.assertEqual(solution.split_by_group(rows, {"b"}), ([rows[0]], rows[1:]))

    def test_missing_group(self):
        with self.assertRaises(ValueError):
            solution.split_by_group([{"id": 1}], {"b"})

    def test_stable_order(self):
        rows = [{"id": 3, "group": "a"}, {"id": 1, "group": "a"}, {"id": 2, "group": "a"}]
        self.assertEqual(solution.split_by_group(rows, set()), (rows, []))


if __name__ == "__main__":
    unittest.main()
