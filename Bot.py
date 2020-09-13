import sys
sys.path.append(".")
from MoveValidator import MoveValidator

class Bot:
    def __init__(self, maze, end_position):
        self.starting_position = [0,0]
        self.moves = 0
        self.current_position = [0,0]
        self.maze = maze
        self.end_position = end_position
        self.validator = MoveValidator(len(self.maze[0]), len(self.maze))

    def get_current_position(self):
        print(self.current_position)

    def move_right(self):
        new_position = self.current_position[0] + 1
        if self.validator.validate_x(new_position):
            self.current_position[0] = new_position
            self.process_movement()

    def move_left(self):
        new_position = self.current_position[0] - 1
        if self.validator.validate_x(new_position):
            self.current_position[0] = new_position
            self.process_movement()

    def move_up(self):
        new_position = self.current_position[1] - 1
        if self.validator.validate_y(new_position):
            self.current_position[1] = new_position
            self.process_movement()

    def move_down(self):
        new_position = self.current_position[1] + 1
        if self.validator.validate_y(new_position):
            self.current_position[1] = new_position
            self.process_movement()

    def process_movement(self):
        self.moves +=1
        print(self.current_position)
