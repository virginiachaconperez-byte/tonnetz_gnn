# Tonnetz GNN

A project exploring how graph neural networks based on the Tonnetz can learn
harmonic representations, predict the next chord, and explain which musical elements
influence their predictions.

The starting design combines a GNN, which processes relationships between notes,
with a GRU, which processes their evolution over time.

## Current status

The project is in its design stage. The repository contains proposals and a
directory structure; there are no datasets, implemented models, tests, or
executable experiments yet.

## Getting started

### Requirements

- Git.
- Python 3.12 for the planned implementation.

### Create a Python environment

From the repository root, on macOS or Linux:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python --version
```

On Windows, using PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe --version
```

On Windows, you can use `.\.venv\Scripts\python.exe` for every Python command
without activating the environment. On macOS and Linux, use `python` after
activation, or `.venv/bin/python` directly.

### Dependencies

The current repository has no Python dependencies to install.

PyTorch, PyTorch Geometric, and a symbolic-music library are candidates for the
implementation; they are not required by the current repository.

### Experiments

Training, evaluation, and test commands are not available yet.

## Repository structure

```text
TonnetzGNN/
├── README.md
├── .gitignore
├── docs/
│   ├── proposal-en.md
│   └── proposal-es.md
├── src/
│   └── tonnetz_gnn/
├── tests/
├── data/
│   └── README.md
├── outputs/
└── report/
    ├── README.md
    ├── figures/
    └── sections/
```

## Datasets and generated files

The dataset has not been selected. [Dataset information](data/README.md) describes
the planned storage layout.

Downloaded data belongs in `data/raw/`, processed data in `data/processed/`,
and experiment results, checkpoints, and logs in `outputs/`. These locations
are ignored by Git.

Small, redistributable test fixtures belong in `tests/fixtures/`. Local
credentials and environment files are also ignored.

## Code organization

The implementation belongs in `src/tonnetz_gnn/`, with tests in `tests/`.
The planned tests cover dataset loading, metadata transformations, annotations,
and format conversions. Evaluation will use separate pieces from training,
with known versions and transpositions grouped in the same split.

## Report and proposals

The project proposal is available in [English](docs/proposal-en.md) and
[Spanish](docs/proposal-es.md).

The [project report](report/README.md) belongs in `report/`, with section
sources in `report/sections/` and figures in `report/figures/`.

## License

A project license has not been selected. Dataset licensing is separate from
the code license.
