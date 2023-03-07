"""This module contains the user game interface."""

from game import Game
from dice import Dice
from player import Player
from dicehand import Dicehand
from intelligence import Intelligence


class UserGame:
    """This class represents the user game."""

    def __init__(self):
        """Initialize the user game."""
        self.game_type = None

    def choose_game_type(self):
        """Choose game type."""
        print(
            """    Choose game mode
    1. Player vs Player
    2. Player vs Computer
    3. Exit"""
            )

        self.game_type = input("Enter your choice(1, 2, 3): ")

    def play(self):
        """Play the game."""
        invalid = True
        while invalid:
            if self.game_type == "1" or self.game_type == "2":
                invalid = False
            elif self.game_type == "3":
                invalid = False
            else:
                print("Invalid choice")
                print("Please choose again(1,2,3)\n")
                self.game_type = input("Enter your choice(1, 2, 3): ")

        if self.game_type == "1":
            self.player_vs_player()
        elif self.game_type == "2":
            self.player_vs_computer()
        elif self.game_type == "3":
            print("Goodbye!")
            print("Thank you for playing")
            print("See you next time")

    def player_vs_computer(self):
        """Player vs computer."""
        target = Game.POINTS_TO_WIN
        choose_name = input("Enter Your name: ")
        player1 = Player("", 0)
        player1.set_name(choose_name)
        player3 = Player("computer", 0)
        dice1 = Dice(6)
        dicehand1 = Dicehand(player1, dice1)
        p1 = dicehand1.which_players_turn()
        dicehand3 = Intelligence(player3, dice1)
        game1 = Game(dicehand1, dicehand3)
        while game1.is_over is not True:
            while dicehand1.turn_over is not True:
                game1.player_play()
                if dicehand1.turn_over is True:
                    game1.start_next_turn()
            while dicehand3.turn_over is not True and p1.has_won is False:
                dicehand3.computer_play()
                if dicehand3.turn_over is True:
                    game1.start_next_turn()
                if dicehand3.which_players_turn().get_total_score() >= target:
                    dicehand3.which_players_turn().has_won = True
                    print(
                        f"\n{dicehand3.which_players_turn().get_name()} \
is winner"
                        )
                    game1.is_over = True
                    break

    def player_vs_player(self):
        choose_name_p1 = input("Enter name (player_1): ")
        player1 = Player("", 0)
        player1.set_name(choose_name_p1)
        choose_name_p2 = input("Enter name (player_2): ")
        player2 = Player("", 0)
        player2.set_name(choose_name_p2)
        dice1 = Dice(6)
        dicehand1 = Dicehand(player1, dice1)
        p1 = dicehand1.which_players_turn()
        dicehand2 = Intelligence(player2, dice1)
        p2 = dicehand2.which_players_turn()
        game1 = Game(dicehand1, dicehand2)
        while game1.is_over is not True:
            while dicehand1.turn_over is not True:
                game1.player_play()
                if dicehand1.turn_over is True and p2.has_won is False:
                    game1.start_next_turn()

            while dicehand2.turn_over is not True and p1.has_won is False:
                game1.player_play()
                if game1.current_turn().turn_over is True:
                    game1.start_next_turn()

    def print_welcome(self):
        """Print welcome message."""
        print("--------------------------------------")
        print("\nWELCOME TO PIG DICE GAME.\n")
        print("--------------------------------------")
        print(
            """Rules:
        The game starts with a roll of the dice.
        Roll the die to accumulate points, but if you roll a 1,
        you lose all points for that turn and
        the turn passes to the next player.
        You can choose to stop rolling and keep your points by holding'.\n
        The first player to reach 100 points wins.\n"""
              )

        input("Press Enter to start the game...")
        print()
