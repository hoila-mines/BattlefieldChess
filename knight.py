from direction import Direction
from piece import Piece
from piece_color import PieceColor


class Knight(Piece):
    def __init__(self, loc_x, loc_y, color):
        super().__init__(loc_x, loc_y, color)
        self.value = 3
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bN.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wN.svg"

    def check_squares(self, board):
        super().check_squares(board)
        vertical_directions = [Direction.UP, Direction.DOWN]
        horizontal_directions = [Direction.LEFT, Direction.RIGHT]
        for direction_y in vertical_directions:
            for direction_x in horizontal_directions:
                super().look_direction(board, [2 * direction_x.value[0], direction_y.value[1]], False)
                super().look_direction(board, [direction_x.value[0], 2 * direction_y.value[1]], False)
