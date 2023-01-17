class Player:
    def __init__(self):
        self.pieces = []
        self.dead_pieces = []
    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)
        self.dead_pieces.append(piece)