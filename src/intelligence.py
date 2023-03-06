"""This module contains the intelligence class for the game pig."""

import dicehand
import random


class intelligence(dicehand.dicehand):
    """This class represents the intelligence of the game pig."""

    def __init__(self, player1, dice1):
        """Initialize the intelligence."""
        super().__init__(player1, dice1)

    def play(self):
        """Play the game."""
        mylist = ["roll", "hold", "roll", "roll"]
        chosen = random.choice(mylist)
        return chosen
