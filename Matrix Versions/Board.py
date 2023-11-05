class Board:
    """
    Board is an object with a width and height
    The board is a dictionary of nodes where the key is the coord position and the value is the Node object
    """

    def __init__(self, h, w, nodes):
        self.width = w
        self.height = h
        self.nodes = nodes

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_node(self, x, y):
        return self.nodes[(x, y)]

    def add_node(self, node):
        self.nodes.add(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def replace_node_color(self, x, y, new_color):
        """
        replaces the color of the node at given coord with given new color
        """
        node = self.nodes[x, y]
        node.set_color(new_color)
        self.nodes[x, y] = node

    def check_node_color(self, x, y, color):
        """
        Boolean, returns True if node at coordinate is the given color
        """
        if self.nodes[(x, y)].get_color() == color:
            return True
        return False

    def print_board(self):
        """
        Prints list of all nodes the board contains using the Node class to_string method
        """
        print("{")
        for n in self.nodes.values():
            print(n.to_string())
        print("}")
