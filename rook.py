from direction import Direction
from piece import Piece
from piece_color import PieceColor


class Rook(Piece):
    def __init__(self, loc_x, locY, color):
        super().__init__(loc_x, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bR.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wR.svg"

    def check_squares(self, board):
        super().check_squares(board)
        directions = [Direction.RIGHT, Direction.UP, Direction.LEFT, Direction.DOWN]
        for direction in directions:
            super().look_direction(board, direction, True)