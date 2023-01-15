from enum import Enum

class Direction(Enum):
    RIGHT = [1, 0]
    RIGHT_UP = [1, 1]
    UP = [0, 1]
    LEFT_UP = [-1, 1]
    LEFT = [-1, 0]
    LEFT_DOWN = [-1, -1]
    DOWN = [0, -1]
    RIGHT_DOWN = [1, -1]
