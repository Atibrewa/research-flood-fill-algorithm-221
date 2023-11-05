class Node():

    def __init__(self, x_coord, y_coord, color):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color

    def get_coord(self):
        return self.x_coord, self.y_coord

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def to_string(self):
        return " (" + str(self.x_coord) + ", " + str(self.y_coord) + ")" + self.color

