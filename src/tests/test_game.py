"""Test the game class."""

import unittest
from dice import Dice
from dicehand import Dicehand
from player import Player
from game import Game


class TestGame(unittest.TestCase):
    """Test the game class."""

    def setUp(self):
        """Set up the game class."""
        self.dice = Dice(6)
        self.player1 = Player("p1", 0)
        self.player2 = Player("p2", 0)
        self.dicehand1 = Dicehand(self.player1, self.dice)
        self.dicehand2 = Dicehand(self.player2, self.dice)
        self.game = Game(self.dicehand1, self.dicehand2)

    def test_current_turn(self):
        """Test the current turn."""
        self.assertEqual(self.game.current_turn(), self.dicehand1)

    def test_start_next_turn(self):
        """Test the start next turn."""
        self.game.start_next_turn()
        self.assertEqual(self.game.current_turn(), self.dicehand2)
        self.game.start_next_turn()
        self.assertEqual(self.game.current_turn(), self.dicehand1)

    # def test_is_over(self):
    #     """Test the is over method."""
    #     self.assertFalse(self.game.is_over())
    #     self.game.current_turn().which_players_turn().set_total_score(100)
    #     self.assertTrue(self.game.is_over())

    def test_player_play(self):
        """Test the player play method."""
        # simulate a game with deterministic rolls
        self.dicehand1.roll = lambda: 5
        self.dicehand2.roll = lambda: 3

        # player1 plays first and holds after first roll
        self.game.player_play()
        self.assertEqual(self.player1.get_total_score(), 5)
        self.assertEqual(self.game.current_turn(), self.dicehand2)

        # player2 rolls twice and holds
        self.game.player_play()
        self.assertEqual(self.player2.get_total_score(), 3)
        self.assertEqual(self.game.current_turn(), self.dicehand1)

        self.game.player_play()
        self.assertEqual(self.player2.get_total_score(), 6)
        self.assertEqual(self.game.current_turn(), self.dicehand1)

        self.game.player_play()
        self.assertEqual(self.player2.get_total_score(), 6)
        self.assertEqual(self.game.current_turn(), self.dicehand1)

        self.game.player_play()
        self.assertEqual(self.player1.get_total_score(), 5)
        self.assertEqual(self.game.current_turn(), self.dicehand2)

        # player1 rolls and gets game-changing 1
        self.dicehand1.roll = lambda: 1
        self.game.player_play()
        self.assertEqual(self.player1.get_total_score(), 0)
        self.assertEqual(self.game.current_turn(), self.dicehand2)

        # player2 rolls and wins the game
        self.dicehand2.roll = lambda: 6
        self.game.player_play()
        self.assertTrue(self.player2.has_won)


if __name__ == '__main__':
    unittest.main()
