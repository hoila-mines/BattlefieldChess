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

    def increment_direction(self, position, direction):
        new_x = position[0] + direction.value[0]  # get square in specified direction
        if self.color is PieceColor.WHITE:  # moving "up" means different directions for the two players
            new_y = position[1] - direction.value[1]
        else:
            new_y = position[1] + direction.value[1]
        return [new_x, new_y]
    def look_direction(self, board, direction, direction_extends, move_type=None):
        keep_iterating = True
        new_x, new_y = self.loc_x, self.loc_y
        while(keep_iterating):
            keep_iterating = direction_extends # if direction does not extend, loop will be run only once
            new_x, new_y = self.increment_direction([new_x, new_y], direction)
            if 0 <= new_x < len(board[0]) and 0 <= new_y < len(board):  # square is in bounds
                new_square_piece = board[new_y][new_x]
                if move_type == MoveType.OCCUPY:  # piece can only move in a direction, not attack (pawns)
                    if new_square_piece is None:  # can only move to empty square
                        self.available_squares.append([new_x, new_y])
                elif move_type == MoveType.CAPTURE:  # piece can only attack in a direction, not move (pawns)
                    if new_square_piece is not None and new_square_piece.color is not self.color:  # can only attack opposing color
                        self.available_squares.append([new_x, new_y])
                        self.attacking_squares.append([new_x, new_y])
                else:  # piece can move and occupy in a direction (default pieces)
                    if new_square_piece is None: # empty square
                        self.available_squares.append([new_x, new_y])
                        self.attacking_squares.append([new_x, new_y])
                    elif new_square_piece.color is not self.color: # enemy square
                        self.available_squares.append([new_x, new_y])
                        self.attacking_squares.append([new_x, new_y])
                        keep_iterating = False
                    else: # friendly square
                        keep_iterating = False
            else:
                keep_iterating = False

    def check_squares(self, board):
        self.available_squares.clear()
        self.attacking_squares.clear()
        pass
