class Game:
    def __init__(self, game_as_str):
        self.id = int(game_as_str.split(":")[0].split(" ")[1])
        self.rounds = []
        for r in game_as_str.split(":")[1].split(";"):
            self.rounds.append(Round(r))

    def get_minimum_number_of_cubes_per_color(self):
        bag = Bag()

        for round in self.rounds:
            if round.red > bag.red:
                bag.red = round.red
            if round.green > bag.green:
                bag.green = round.green
            if round.blue > bag.blue:
                bag.blue = round.blue

        return bag.get_contents()


class Round:
    def __init__(self, round_as_str) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0

        for balls in round_as_str.split(","):
            number, color = balls.strip().split(" ")
            if color == "red":
                self.red = int(number)
            elif color == "green":
                self.green = int(number)
            elif color == "blue":
                self.blue = int(number)
            else:
                raise Exception("Invalid color")


class Bag:
    def __init__(self) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0

    def get_contents(self):
        return [self.red, self.green, self.blue]
