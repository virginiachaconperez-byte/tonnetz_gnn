"""Validate a TOML configuration and save a JSON snapshot."""

import argparse
from pathlib import Path

from tonnetz_gnn.config import load_config, save_config


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True, help="Input TOML file.")
    parser.add_argument("--output", type=Path, required=True, help="New JSON snapshot.")
    args = parser.parse_args()

    try:
        config = load_config(args.config)
        save_config(config, args.output)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    print(f"Validated settings saved to {args.output}")


if __name__ == "__main__":
    main()
