from move_type import MoveType
from piece_color import PieceColor

class Piece:
    spriteLoc = ""

    def __init__(self, loc_x, loc_y, color):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.color = color
        self.is_highlighted = False
        self.attacking_squares = []
        self.available_squares = []

    def set_loc(self, loc_x, loc_y):
        self.loc_x = loc_x
        self.loc_y = loc_y

    def add_highlight(self):
        self.is_highlighted = True

    def remove_highlight(self):
        self.is_highlighted = False

    def look_direction(self, board, direction, move_type = None):
        newX = self.loc_x + direction.value[0]  # get square in specified direction
        if self.color is PieceColor.WHITE: # moving "up" means different directions for the two players
            newY = self.loc_y - direction.value[1]
        else:
            newY = self.loc_y + direction.value[1]
        if 0 <= newX < len(board[0]) and 0 <= newY < len(board):  # square is in bounds
            new_square_piece = board[newY][newX]
            if move_type == MoveType.OCCUPY: # piece can only move in a direction, not attack (pawns)
                if new_square_piece is None: # can only move to empty square
                    self.available_squares.append([newX, newY])
                    # print("added occupy " + str(self.color) + " " + str(newY))
            elif move_type == MoveType.CAPTURE: # piece can only attack in a direction, not move (pawns)
                if new_square_piece is not None and new_square_piece.color is not self.color: # can only attack opposing color
                    self.available_squares.append([newX, newY])
                    self.attacking_squares.append([newX, newY])
                    # print("added capture")
            else: # piece can move and occupy in a direction (default pieces)
                if new_square_piece is None or new_square_piece.color is not self.color:
                    # print("added generic")
                    self.available_squares.append([newX, newY])
                    self.attacking_squares.append([newX, newY])

    def check_squares(self, board):
        self.available_squares.clear()
        self.attacking_squares.clear()
        pass
