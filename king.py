from piece import Piece
from piece_color import PieceColor


class King(Piece):
    def __init__(self, locX, locY, color):
        super().__init__(locX, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bK.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wK.svg"
    def calculate_squares(self):
        pass