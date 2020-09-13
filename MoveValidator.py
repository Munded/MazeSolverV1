class MoveValidator:
    def __init__(self, x_length, y_length):
        self.max_x_length = x_length
        self.max_y_length = y_length

    def validate_x(self, new_position):
        success = True
        if new_position > self.max_x_length or new_position < 0 :
            print("You hit a wall")
            success = False
        return success

    def validate_y(self, new_position):
        success = True
        if new_position > self.max_y_length or new_position < 0:
            print("You hit a wall")
            success = False
        return success
