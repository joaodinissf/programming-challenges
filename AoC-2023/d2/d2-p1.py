import Game
import GameCriteria


def get_possible_games(games, game_criteria):
    ids_of_possible_games = []

    for game_as_str in games:
        game = Game.Game(game_as_str)
        if game_criteria.is_game_possible(game):
            ids_of_possible_games.append(game.id)

    return ids_of_possible_games


def solve(input_file, game_criteria):
    games = input_file.readlines()
    ids_of_possible_games = get_possible_games(games, game_criteria)
    return sum(ids_of_possible_games)


def main():
    game_criteria = GameCriteria.GameCriteria(12, 13, 14)
    file_name = "d2/d2-p1-sample.txt"
    file_name = "d2/d2-p1.txt"
    with open(file_name, "r") as f:
        print(solve(f, game_criteria))


if __name__ == "__main__":
    main()
