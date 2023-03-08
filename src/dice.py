"""This module contains the dice class."""
import random


class Dice:
    """This class represents a dice."""

    def __init__(self, dice):
        """Initialize the dice."""
        self.dice = dice

    def roll_dice(self):
        """Roll the dice."""
        return random.randint(1, self.get_dice())

    def set_dice(self, dice):
        """Initialize the dice."""
        self.dice = dice

    def get_dice(self):
        """Return the dice face."""
        return self.dice

    def __str__(self) -> str:
        return f"Dice faces are {self.dice}"
