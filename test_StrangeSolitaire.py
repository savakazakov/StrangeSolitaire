import unittest
import random
import copy
from StrangeSolitaire import create_deck, matches, quick_check, shuffle_deck, solve


class TestStrangeSolitaire(unittest.TestCase):
    def setUp(self):
        self.deck = create_deck()

    # def test_create_deck(self):
    #     self.assertEqual(len(self.deck), 52)
    #     self.assertIn(["AH"], self.deck)
    #     self.assertIn(["2D"], self.deck)

    def test_matches(self):
        self.assertTrue(matches(["2H"], ["2D"]))
        self.assertTrue(matches(["2H"], ["3H"]))
        self.assertFalse(matches(["2H"], ["3D"]))

    def test_shuffle_deck(self):
        deck_copy = self.deck.copy()
        shuffled_deck = shuffle_deck(deck_copy)
        self.assertNotEqual(self.deck, shuffled_deck)

    def test_quick_check(self):
        for _ in range(1000):
            deck = shuffle_deck(create_deck())
            _, solve_result = solve(copy.deepcopy(deck))
            quick_solve_result = quick_check(copy.deepcopy(deck))
            if quick_solve_result == False:
                self.assertEqual(solve_result, False)


if __name__ == "__main__":
    unittest.main()
