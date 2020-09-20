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
        self.finished = False

    def get_current_position(self):
        print(self.current_position)

    #Horizontal Movement
    def move_right(self):
        new_position = self.current_position[0] + 1
        self.move_horizontal(new_position)

    def move_left(self):
        new_position = self.current_position[0] - 1
        self.move_horizontal(new_position)

    def move_horizontal(self, new_position):
        if not self.finished and self.validator.validate_x(new_position):
            self.current_position[0] = new_position
            self.process_movement()

    #Vertical Movement
    def move_up(self):
        new_position = self.current_position[1] - 1
        self.move_vertical(new_position)

    def move_down(self):
        new_position = self.current_position[1] + 1
        self.move_vertical(new_position)

    def move_vertical(self, new_position):
        if not self.finished and self.validator.validate_y(new_position):
            self.current_position[1] = new_position
            self.process_movement()

    #post-movement processing
    def process_movement(self):
        if self.current_position[0] == self.end_position[0] and self.current_position[1] == self.end_position[1]:
            print("You Won")
            self.finished = True
        else:
            self.moves +=1
            print(self.current_position)
