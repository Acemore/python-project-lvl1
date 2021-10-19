#!/usr/bin/env python3

from brain_games.engine import run_game
import brain_games.games.calc as brain_game_calc


def main():
    run_game(brain_game_calc)


if __name__ == "__main__":
    main()
