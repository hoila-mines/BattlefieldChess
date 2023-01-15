from peice_color import PieceColor
class Piece:
    available_squares = []
    color = None
    spriteLoc = ""

    def __init__(self, locX, locY, color):
        self.locX = locX
        self.locY = locY
        self.color = color
        self.is_highlighted = False
    def set_loc(self, locX, locY):
        self.locX = locX
        self.locY = locY