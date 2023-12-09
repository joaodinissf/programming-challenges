import math
import Game
import GameCriteria


def get_possible_games(games, game_criteria):
    ids_of_possible_games = []

    for game_as_str in games:
        game = Game.Game(game_as_str)
        if game_criteria.is_game_possible(game):
            ids_of_possible_games.append(game.id)

    return ids_of_possible_games


def get_powers_games(games):
    powers_of_games = []

    for game_as_str in games:
        game = Game.Game(game_as_str)
        powers_of_games.append(math.prod(game.get_minimum_number_of_cubes_per_color()))

    return powers_of_games


def solve(input_file):
    games = input_file.readlines()
    ids_of_possible_games = get_powers_games(games)
    return sum(ids_of_possible_games)


def main():
    file_name = "d2/d2-p1-sample.txt"
    file_name = "d2/d2-p1.txt"
    with open(file_name, "r") as f:
        print(solve(f))


if __name__ == "__main__":
    main()
