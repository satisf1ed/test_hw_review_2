from dataclasses import dataclass


TOKENIZER_NAME = "ai-forever/rugpt3small_based_on_gpt2"
MAX_LENGTH = 512
VALIDATION_SIZE = 5000
MAX_TRAINING_SECONDS = 30 * 60


@dataclass(frozen=True)
class TrainingConfig:
    batch_size: int
    gradient_accumulation_steps: int
    learning_rate: float
    scheduler: str
    optimizer: str
    bf16: bool = True
    tf32: bool = True
    torch_compile: bool = True

    @property
    def effective_batch_size(self) -> int:
        return self.batch_size * self.gradient_accumulation_steps


EXPERIMENTS = (
    TrainingConfig(4, 8, 3e-4, "cosine", "adamw_torch_fused"),
    TrainingConfig(8, 4, 5e-4, "linear", "adamw_torch_fused"),
    TrainingConfig(8, 4, 8.7e-4, "constant", "adamw_torch_fused"),
)


def split_indices(dataset_size: int) -> tuple[range, range]:
    """Return the required deterministic validation and train ranges."""
    if dataset_size <= VALIDATION_SIZE:
        raise ValueError("dataset must contain more than 5000 samples")
    validation = range(0, VALIDATION_SIZE)
    train = range(VALIDATION_SIZE, dataset_size)
    return train, validation


def validate_experiment(config: TrainingConfig) -> None:
    if config.batch_size <= 0 or config.gradient_accumulation_steps <= 0:
        raise ValueError("batch sizes must be positive")
    if not 0 < config.learning_rate < 1:
        raise ValueError("learning rate must be between zero and one")
    if config.scheduler not in {"linear", "cosine", "constant"}:
        raise ValueError("unsupported scheduler")


if __name__ == "__main__":
    for experiment in EXPERIMENTS:
        validate_experiment(experiment)
        print(experiment)
