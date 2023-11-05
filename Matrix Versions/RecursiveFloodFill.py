import time
from Node import Node
from Board import Board

##Boards
board = [
    ["B", "B", "B", "B", "B", "B", "B", "B", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "W", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "W", "B"],
    ["B", "W", "W", "B", "W", "W", "W", "W", "B"],
    ["B", "B", "B", "W", "W", "W", "B", "B", "B"],
    ["B", "W", "W", "W", "W", "B", "W", "W", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "W", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "W", "B"],
    ["B", "B", "B", "B", "B", "B", "B", "B", "B"]
    ]
board2 = [
    ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
    ["B", "W", "W", "W", "W", "W", "W", "W", "W", "W", "B", "W", "W", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "W", "W", "W", "B", "W", "W", "B"],
    ["B", "W", "W", "B", "W", "W", "W", "W", "W", "W", "B", "W", "W", "B"],
    ["B", "B", "B", "W", "W", "W", "B", "W", "W", "W", "W", "W", "W", "B"],
    ["B", "W", "W", "W", "W", "B", "W", "W", "W", "W", "W", "W", "W", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "B", "B", "B", "B", "W", "W", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "B", "W", "W", "W", "B", "W", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "B", "W", "W", "W", "B", "B", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "B", "W", "W", "W", "B", "W", "B"],
    ["B", "W", "W", "B", "W", "W", "W", "B", "W", "W", "B", "B", "W", "B"],
    ["B", "W", "B", "B", "B", "B", "B", "B", "W", "W", "B", "W", "W", "B"],
    ["B", "B", "W", "W", "W", "B", "W", "B", "W", "W", "B", "W", "W", "B"],
    ["B", "W", "W", "W", "B", "W", "W", "B", "W", "W", "B", "W", "W", "B"],
    ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]
    ]
board0 = [
    ["B", "B", "B", "B"],
    ["B", "W", "W", "B"],
    ["B", "W", "W", "B"],
    ["B", "B", "B", "B"]
    ]
node_dic = {
    (0, 0): Node(0, 0, "B"), (0, 1): Node(0, 1, "B"), (0, 2): Node(0, 2, "B"), (0, 3): Node(0, 3, "B"),
    (1, 0): Node(1, 0, "B"), (1, 1): Node(1, 1, "W"), (1, 2): Node(1, 2, "W"), (1, 3): Node(1, 3, "B"),
    (2, 0): Node(2, 0, "B"), (2, 1): Node(2, 1, "W"), (2, 2): Node(2, 2, "W"), (2, 3): Node(2, 3, "B"),
    (3, 0): Node(3, 0, "B"), (3, 1): Node(3, 1, "B"), (3, 2): Node(3, 2, "B"), (3, 3): Node(3, 3, "B")
    }
nodeBoard = Board(4, 4, node_dic)


##---- helper functions
def print_board(board):
    """
    Prints array implementation of board nicely
    """
    for a in board:
        print(a)

def check_node(coord, board, struc):
    """
    adds coord to given data structure only if its color is "W"
    """
    if (board[coord[0]][coord[1]]) == "W":
        struc.append(coord)
        return True
    return False


#---- Flood Fill algorithms- Array Implementation
def floodFill1(startA, startB, newColor, board):
    """
    recursive implementation, 4 directional
    pseudocode: https://en.wikipedia.org/wiki/Flood_fill
    """
    if (startA > len(board)) or (startB > len(board[0])):
        return
    elif (startA < 0) or (startB < 0):
        return
    if board[startA][startB] == "W":
        board[startA][startB] = newColor
        floodFill1(startA -1, startB, newColor, board)
        floodFill1(startA +1, startB, newColor, board)
        floodFill1(startA, startB -1, newColor, board)
        floodFill1(startA, startB +1, newColor, board)
        return


def floodFill2(startA, startB, newColor, board):
    """
    stack implementation
    """
    stack = []
    stack.append((startA, startB))
    while len(stack) > 0:
        pos = stack.pop()
        node = board[pos[0]][pos[1]]
        if node == "W":
            board[pos[0]][pos[1]] = newColor
            stack.append((pos[0] - 1, pos[1]))
            stack.append((pos[0] + 1, pos[1]))
            stack.append((pos[0], pos[1] -1))
            stack.append((pos[0], pos[1] +1))
    return board

def floodFill2b(startA, startB, newColor, board):
    """
    stack implementation
    optimized to only add a node to the stack if it's the target color
    """
    stack = []
    stack.append((startA, startB))
    while len(stack) > 0:
        pos = stack.pop()
        node = board[pos[0]][pos[1]]
        if node == "W":
            board[pos[0]][pos[1]] = newColor
            check_node((pos[0] -1, pos[1]), board, stack)
            check_node((pos[0] +1, pos[1]), board, stack)
            check_node((pos[0], pos[1] -1), board, stack)
            check_node((pos[0], pos[1] +1), board, stack)
    return board

def floodFill3(startA, startB, newColor, board):
    """
    queue implementation
    """
    queue = []
    queue.append((startA, startB))
    while len(queue) > 0:
        pos = queue.pop(0)
        node = board[pos[0]][pos[1]]
        if node == "W":
            board[pos[0]][pos[1]] = newColor
            queue.append((pos[0] -1, pos[1]))
            queue.append((pos[0] +1, pos[1]))
            queue.append((pos[0], pos[1] -1))
            queue.append((pos[0], pos[1] +1))
    return board


#---- Flood Fill algorithms using Node & Board Obects

def floodFill1_2(startA, startB, newColor, board):
    """
    using Node class
    recursive implementation, 4 directional
    pseudocode: https://en.wikipedia.org/wiki/Flood_fill
    """
    if (startA > board.get_width()) or (startB > board.get_height()):
        return
    elif (startA < 0) or (startB < 0):
        return

    if board.check_node_color(startA, startB, "W"):
        board.replace_node_color(startA, startB, newColor)

        floodFill1_2(startA -1, startB, newColor, board)
        floodFill1_2(startA +1, startB, newColor, board)
        floodFill1_2(startA, startB -1, newColor, board)
        floodFill1_2(startA, startB +1, newColor, board)
        return

def floodFill2_2(startA, startB, newColor, board):
    """
    using Node objects
    stack implementation
    """
    stack = []
    stack.append((startA, startB))
    while len(stack) > 0:
        pos = stack.pop()
        if board.check_node_color(pos[0], pos[1], "W"):
            board.replace_node_color(pos[0], pos[1], newColor)
            stack.append((pos[0] -1, pos[1]))
            stack.append((pos[0] +1, pos[1]))
            stack.append((pos[0], pos[1] -1))
            stack.append((pos[0], pos[1] +1))
    return board

def floodFill3_2(startA, startB, newColor, board):
    """
    using Node objects
    queue implementation
    """
    queue = []
    queue.append((startA, startB))
    while len(queue) > 0:
        pos = queue.pop(0)
        if board.check_node_color(pos[0], pos[1], "W"):
            board.replace_node_color(pos[0], pos[1], newColor)
            queue.append((pos[0] -1, pos[1]))
            queue.append((pos[0] +1, pos[1]))
            queue.append((pos[0], pos[1] -1))
            queue.append((pos[0], pos[1] +1))
    return board


#running tests on array implemetation
# start_time0 = time.time()
# floodFill3(2, 2, "R", board0)
# end_time0 = time.time()
# print("time", end_time0 - start_time0)
# print_board(board0)


#running tests on node object implemetation
start_time1 = time.time()
floodFill3_2(2, 2, "R", nodeBoard)
end_time1 = time.time()
nodeBoard.print_board()
print("time", end_time1 - start_time1)


'''
1: time 0.0002999305725097656

2:  time 0.00018405914306640625
    time 0.0003650188446044922
    time 0.0003299713134765625
    time 0.0006148815155029297
    time 0.0003108978271484375
    time 0.000247955322265625

2b: time 0.0005712509155273438
    time 0.00035190582275390625
    time 0.00039696693420410156
    time 0.0004279613494873047
    time 0.0002999305725097656

3: time 0.0002300739288330078

'''




