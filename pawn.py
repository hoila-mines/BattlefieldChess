from direction import Direction
from move_type import MoveType
from piece import Piece
from piece_color import PieceColor


class Pawn(Piece):
    def __init__(self, locX, locY, color):
        super().__init__(locX, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bP.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wP.svg"

    def check_squares(self, board):
        super().look_direction(board, Direction.UP, MoveType.OCCUPY)
        super().look_direction(board, Direction.RIGHT_UP, MoveType.CAPTURE)
        super().look_direction(board, Direction.LEFT_UP, MoveType.CAPTURE)
