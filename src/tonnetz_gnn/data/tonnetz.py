"""Pitch-class graph of the classical Tonnetz.

Reference: Catanzaro (2011), Generalized Tonnetze, Introduction.
https://arxiv.org/abs/1612.03519
"""


def build_tonnetz() -> dict[int, tuple[int, ...]]:
    """Return an undirected Tonnetz as a dictionary of sorted neighbours.

    Nodes are the twelve chromatic pitch classes, from 0 (C) to 11 (B).
    Octaves and enharmonic spellings share nodes. Connections represent
    minor thirds, major thirds and perfect fifths in either direction.
    """
    intervals = (-7, -4, -3, 3, 4, 7)
    return {
        pitch_class: tuple(
            sorted((pitch_class + interval) % 12 for interval in intervals)
        )
        for pitch_class in range(12)
    }
