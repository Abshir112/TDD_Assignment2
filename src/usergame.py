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
        self.target = Game.POINTS_TO_WIN
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
        choice = ["1", "2", "3"]
        while invalid:
            if self.game_type in choice:
                invalid = False
            else:
                print("\nInvalid choice")
                print("Please choose again(1,2,3)\n")
                self.game_type = input("Enter your choice(1, 2, 3): ")

        if self.game_type == "1":
            self.player_vs_player()
        elif self.game_type == "2":
            self.player_vs_computer()
        else:
            print("\nGoodbye!")
            print("Thank you for playing")
            print("See you next time")

    def player_vs_computer(self):
        """Player vs computer."""
        player1 = Player("", 0)
        player3 = Player("Computer", 0)
        dice1 = Dice(6)
        choose_name = input("\nEnter Your name: ")
        player1.set_name(choose_name.upper())
        dicehand1 = Dicehand(player1, dice1)
        dicehand3 = Intelligence(player3, dice1)
        game1 = Game(dicehand1, dicehand3)
        while game1.is_over is not True:
            while dicehand1.turn_over is not True:
                game1.player_play()
                if dicehand1.turn_over is True:
                    game1.start_next_turn()
            player_1_won = player1.has_won
            while dicehand3.turn_over is False and player_1_won is False:
                dicehand3.computer_play()
                if dicehand3.turn_over is True:
                    game1.start_next_turn()
                if player3.get_total_score() >= self.target:
                    dicehand3.which_players_turn().has_won = True
                    print("\nCongratulations!")
                    print(
                        f"{dicehand3.which_players_turn().get_name()} \
is the winner"
                    )
                    game1.is_over = True
                    break

    def player_vs_player(self):
        """Player vs Player game."""
        player1 = Player("", 0)
        playe2 = Player("", 0)
        dice1 = Dice(6)
        dicehand2 = Dicehand(playe2, dice1)
        choose_name_p1 = input("\nEnter name (player_1): ")
        player1.set_name(choose_name_p1.upper())
        choose_name_p2 = input("Enter name (player_2): ")
        playe2.set_name(choose_name_p2.upper())
        dicehand1 = Dicehand(player1, dice1)
        player1 = dicehand1.which_players_turn()
        playe2 = dicehand2.which_players_turn()
        game1 = Game(dicehand1, dicehand2)
        while game1.is_over is not True:
            while dicehand1.turn_over is not True:
                game1.player_play()
                dicehand_1 = dicehand1.turn_over
                if dicehand_1 is True and playe2.has_won is False:
                    game1.start_next_turn()

            dicehand_2 = dicehand2.turn_over
            while dicehand_2 is not True and player1.has_won is False:
                game1.player_play()
                if game1.current_turn().turn_over is True:
                    game1.start_next_turn()
                if playe2.get_total_score() >= self.target:
                    dicehand2.which_players_turn().has_won = True
                    game1.is_over = True
                    break

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
