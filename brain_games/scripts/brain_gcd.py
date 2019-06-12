# -*- coding: utf-8 -*-

"""Brain gcd game."""

from brain_games.games.brain_gcd import make_question
from brain_games.scripts.brain_games import game_engine

QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    """Run even game."""
    game_engine(QUESTION, make_question)


if __name__ == '__main__':
    main()