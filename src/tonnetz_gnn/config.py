"""Load and record experiment settings."""

from pathlib import Path
import tomllib

from pydantic import BaseModel, ConfigDict, Field


class ExperimentConfig(BaseModel):
    """Required settings, with strict types and no unknown fields."""

    model_config = ConfigDict(extra="forbid", strict=True)

    dataset_path: str = Field(min_length=1, pattern=r"\S")
    seed: int = Field(ge=0)
    context_length: int = Field(gt=0)


def load_config(path: Path) -> ExperimentConfig:
    """Read a TOML file and validate its settings."""
    with path.open("rb") as source:
        return ExperimentConfig.model_validate(tomllib.load(source))


def save_config(config: ExperimentConfig, path: Path) -> None:
    """Save a validated JSON snapshot without overwriting an existing file."""
    content = config.model_dump_json(indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as destination:
        destination.write(content)
