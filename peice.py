from peice_color import PieceColor
class Piece:
    locX, locY = 0, 0
    available_squares = []
    color = PieceColor.BLACK
    spriteLoc = ""

    def __init__(self, locX, locY, color):
        self.locX = locX
        self.locY = locY
        self.color = color
    def set_loc(self, locX, locY):
        self.locX = locX
        self.locY = locY