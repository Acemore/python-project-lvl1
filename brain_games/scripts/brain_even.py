#!/usr/bin/env python3

from brain_games.engine import run_game
import brain_games.games.even as brain_game_even


def main():
    run_game(brain_game_even)


if __name__ == '__main__':
    main()
