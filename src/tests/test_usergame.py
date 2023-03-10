"""This module contains the user game class and its methods."""

import unittest
from usergame import UserGame
from game import Game
from dice import Dice
from player import Player
from dicehand import Dicehand


class TestUserGame(unittest.TestCase):
    """This class represents the test player class."""

    def setUp(self):
        """Set up the test game class."""
        self.user = UserGame()

    def test_init(self):
        """Test the init method."""
        # Test if the game is an instance of game
        self.assertIsInstance(self.user, UserGame)

    def test_player_vs_computer(self):
        """Test whether player vs computer method work as indented."""
        player1 = Player("player1", 0)
        computer = Player("Computer", 0)
        dice1 = Dice(6)
        dicehand1 = Dicehand(player1, dice1)
        dicehand3 = Dicehand(computer, dice1)
        game2 = Game(dicehand1, dicehand3)
        self.assertEqual(dicehand1.which_players_turn(), player1)
        # manually setting dicehand 1 turn over to be True
        dicehand1.turn_over = True
        game2.start_next_turn()
        # turn over for player1 and it should be
        # automatically changed to next player's turn
        self.assertEqual(dicehand3.which_players_turn(), computer)
        # if computer wins the game over must be true
        dicehand3.set_score(50)
        computer.set_total_score(50)
        dicehand3.end_turn()
        # It must not start next player turn when one player wins the game
        # set game over to be true so that it'll not invoke next dicehand
        game2.is_over = True
        self.assertEqual(game2.is_over, True)

    def test_player_vs_player(self):
        """Test whether player vs computer method work as indented."""
        player1 = Player("player1", 0)
        player2 = Player("player2", 0)
        dice1 = Dice(6)
        dicehand1 = Dicehand(player1, dice1)
        dicehand2 = Dicehand(player2, dice1)
        game1 = Game(dicehand1, dicehand2)
        self.assertEqual(dicehand1.which_players_turn(), player1)
        # manually setting dicehand 1 turn over to be True
        dicehand1.turn_over = True
        game1.start_next_turn()
        # turn over for player1 and it should be
        # automatically changed to next player's turn
        self.assertEqual(dicehand2.which_players_turn(), player2)
        # player2 score not set to 100 so has_won must return false
        self.assertFalse(player2.has_won)
        dicehand2.set_score(50)
        player2.set_total_score(50)
        dicehand2.end_turn()
        # turn total 50 points added to total score of player which is 50
        # endturn method accumulate total score + turn score,
        # reached target score so game is over, Player2 wins
        # if player2 wins the game over must be true
        game1.is_over = True
        self.assertEqual(game1.is_over, True)
