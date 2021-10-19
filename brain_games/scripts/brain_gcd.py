#!/usr/bin/env python3

from brain_games.engine import run_game
import brain_games.games.gcd as brain_game_gcd


def main():
    run_game(brain_game_gcd)


if __name__ == "__main__":
    main()
