class Player:
    def __init__(self, color):
        self.pieces = []
        self.dead_pieces = []
        self.color = color
    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)
        self.dead_pieces.append(piece)