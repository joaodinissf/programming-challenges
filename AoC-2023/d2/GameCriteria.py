from Game import Game, Round


class GameCriteria:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def is_round_possible(self, round: Round):
        return (
            round.red <= self.red
            and round.green <= self.green
            and round.blue <= self.blue
        )

    def is_game_possible(self, game: Game):
        for round in game.rounds:
            if not self.is_round_possible(round):
                return False
        return True
