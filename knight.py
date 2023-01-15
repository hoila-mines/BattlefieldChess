from peice import Piece
from peice_color import PieceColor


class Knight(Piece):
    def __init__(self, locX, locY, color):
        super().__init__(locX, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bN.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wN.svg"
    def calculate_squares(self):
        pass