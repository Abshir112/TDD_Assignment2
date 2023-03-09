"""This module is the main module of the game."""

from usergame import UserGame


def main():
    """Run the program."""
    user_game1 = UserGame()

    user_game1.print_welcome()
    user_game1.choose_game_type()
    user_game1.play()


if __name__ == "__main__":
    main()
