# Tonnetz GNN

A project studying whether harmonic relationships represented by the Tonnetz
can improve next-chord prediction with graph neural networks. It also evaluates
explanations of the model's predictions.

The project is in early development. Package installation is available;
data preparation and experiments are not implemented yet.

## Installation

Requires Git and Python 3.12.

Clone the repository:

```sh
git clone https://github.com/virginiachaconperez-byte/tonnetz_gnn.git TonnetzGNN
cd TonnetzGNN
```

On macOS or Linux:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -c "import tonnetz_gnn; print(tonnetz_gnn.__file__)"
```

On Windows, using PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -c "import tonnetz_gnn; print(tonnetz_gnn.__file__)"
```

The last command should print the path to `src/tonnetz_gnn/__init__.py`.

## Repository structure

```text
TonnetzGNN/
├── README.md
├── .gitignore
├── pyproject.toml
├── docs/
│   ├── proposal-en.md
│   └── proposal-es.md
├── src/
│   └── tonnetz_gnn/
│       └── __init__.py
├── tests/
├── data/
│   └── README.md
├── outputs/
└── report/
    ├── README.md
    ├── figures/
    └── sections/
```

## Data

The first pilot uses the DCML Annotated Mozart Sonatas corpus.
Dataset files are not included in this repository. See
[dataset instructions](data/README.md) for download steps, file locations,
and licensing information.

## Documentation

- [Project proposal in English](docs/proposal-en.md)
- [Project proposal in Spanish](docs/proposal-es.md)

## License

A code license has not been selected. Dataset licensing is separate.
