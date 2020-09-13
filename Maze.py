import sys
sys.path.append(".")
import Bot

class Maze:
    def __init__(self):
        x_length = 5
        y_length = 5
        self.layout = self.generate_grid(x_length, y_length)
        self.start_position = [0,0]
        self.end_position = [x_length, y_length]
        self.competitors = []


    def generate_grid(self, x_length, y_length):
        grid = []
        row = []

        for i in range(x_length):
            row.append(0)

        for i in range(y_length):
            grid.append(row)

        print(grid)
        return grid

    def add_bot(self):
        newBot = Bot.Bot(self.layout, self.end_position)
        self.competitors.append(newBot)
