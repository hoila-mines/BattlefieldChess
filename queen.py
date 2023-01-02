from peice import Piece
from peice_color import PieceColor


class Queen(Piece):
    def __init__(self, locX, locY, color):
        super().__init__(locX, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bQ.png"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wQ.png"
    def calculate_squares(self):
        pass