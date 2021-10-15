#!/usr/bin/env python3

from brain_games.brain_games_engine import run_game
import brain_games.games.brain_game_calc as brain_game_calc


def main():
    run_game(brain_game_calc)


if __name__ == "__main__":
    main()
