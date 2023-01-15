from piece import Piece
from piece_color import PieceColor


class King(Piece):
    def __init__(self, loc_x, locY, color):
        super().__init__(loc_x, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bK.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wK.svg"
    def calculate_squares(self):
        pass