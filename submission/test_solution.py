import unittest

from solution import EXPERIMENTS, VALIDATION_SIZE, split_indices, validate_experiment


class SolutionTest(unittest.TestCase):
    def test_first_5000_samples_are_reserved_for_validation(self) -> None:
        train, validation = split_indices(6000)
        self.assertEqual(validation, range(0, VALIDATION_SIZE))
        self.assertEqual(train, range(VALIDATION_SIZE, 6000))

    def test_small_dataset_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "more than 5000"):
            split_indices(VALIDATION_SIZE)

    def test_experiment_grid_is_valid(self) -> None:
        for experiment in EXPERIMENTS:
            with self.subTest(experiment=experiment):
                validate_experiment(experiment)
                self.assertEqual(experiment.effective_batch_size, 32)


if __name__ == "__main__":
    unittest.main()
