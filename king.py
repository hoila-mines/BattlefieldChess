from peice import Piece
from peice_color import PieceColor


class King(Piece):
    def __init__(self, locX, locY, color):
        super().__init__(locX, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bK.png"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wK.png"
    def calculate_squares(self):
        pass