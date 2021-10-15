#!/usr/bin/env python3

from brain_games.brain_games_engine import run_game
import brain_games.games.brain_game_gcd as brain_game_gcd


def main():
    run_game(brain_game_gcd)


if __name__ == "__main__":
    main()
