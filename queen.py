from direction import Direction
from piece import Piece
from piece_color import PieceColor


class Queen(Piece):
    def __init__(self, loc_x, loc_y, color):
        super().__init__(loc_x, loc_y, color)
        self.value = 9
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bQ.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wQ.svg"

    def check_squares(self, board):
        super().check_squares(board)
        for direction in Direction:
            super().look_direction(board, direction, True)