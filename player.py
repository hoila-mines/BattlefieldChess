class Player:
    is_player_turn = False
    def __init__(self):
        self.pieces = []
    def add_piece(self, piece):
        self.pieces.append(piece)