"""Checks for the musical relationships in the Tonnetz graph."""

from itertools import combinations
import unittest

from tonnetz_gnn.data.tonnetz import build_tonnetz


class TonnetzTests(unittest.TestCase):
    def test_graph_structure_and_musical_examples(self):
        graph = build_tonnetz()
        self.assertEqual(set(graph), set(range(12)))
        self.assertEqual(graph[0], (3, 4, 5, 7, 8, 9))
        self.assertEqual(sum(len(neighbours) for neighbours in graph.values()), 72)
        triads = {
            "C major": (0, 4, 7),
            "C minor": (0, 3, 7),
            "B major": (11, 3, 6),
        }
        for name, notes in triads.items():
            with self.subTest(chord=name):
                for first, second in combinations(notes, 2):
                    self.assertIn(second, graph[first])

    def test_transposition_preserves_every_connection(self):
        graph = build_tonnetz()
        for shift in range(12):
            with self.subTest(shift=shift):
                expected = tuple(sorted((note + shift) % 12 for note in graph[0]))
                self.assertEqual(graph[shift], expected)
