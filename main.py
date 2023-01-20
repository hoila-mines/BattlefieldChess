import math

import pygame

import pygame.display
import pygame.image

from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from piece_color import PieceColor
from player import Player
from queen import Queen
from rook import Rook

# setup game window
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1078, 820
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Battlefield Chess")
FPS_LIMIT = 60
# calculate board start and square size
BOARD_WIDTH, BOARD_HEIGHT = 22, 12
SQUARE_SIZE = min(WINDOW_WIDTH / BOARD_WIDTH, WINDOW_HEIGHT / BOARD_HEIGHT)
Y_OFFSET = (WINDOW_HEIGHT - SQUARE_SIZE * BOARD_HEIGHT) / 2
# define colors
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 128, 128)
HIGHLIGHT_COLOR = (51, 153, 255)
# initiate players and board
white_player = Player(PieceColor.WHITE)
black_player = Player(PieceColor.BLACK)
players = [white_player, black_player]
player_turn = PieceColor.WHITE
board = [[None for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
# highlighted_piece = None
image_cache = {}
pygame.font.init()
font = pygame.font.Font(None, 40)

board_config = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bN", "bB", "bQ", "bK",
     "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",
     "bP", "bP", "bP"],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP",
     "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "wN", "wB", "wQ", "wK",
     "wB", "wN", "wR"]
]


def read_config():
    for i in range(len(board_config)):  # read through each row
        if len(board_config[i]) == 0:  # if the array element is empty, there are no pieces to read
            continue
        else:
            for j in range(len(board_config[i])):  # read through each column
                # get piece info in character representation
                piece_color_char = board_config[i][j][0]
                piece_type_char = board_config[i][j][1]
                piece_color = None
                newPiece = None

                if piece_color_char == 'w':  # get the piece color
                    piece_color = PieceColor.WHITE
                elif piece_color_char == 'b':
                    piece_color = PieceColor.BLACK

                match piece_type_char:  # get the piece type and instantiate it
                    case 'R':
                        newPiece = Rook(j, i, piece_color)
                    case 'N':
                        newPiece = Knight(j, i, piece_color)
                    case 'B':
                        newPiece = Bishop(j, i, piece_color)
                    case 'K':
                        newPiece = King(j, i, piece_color)
                    case 'Q':
                        newPiece = Queen(j, i, piece_color)
                    case 'P':
                        newPiece = Pawn(j, i, piece_color)
                # add piece to correct player
                if piece_color == PieceColor.WHITE:
                    white_player.add_piece(newPiece)
                    # white_player.dead_pieces.append(newPiece)
                elif piece_color == PieceColor.BLACK:
                    black_player.add_piece(newPiece)
                    # black_player.dead_pieces.append(newPiece)
                board[i][j] = newPiece


def alternate_white_red(color):  # swap the color from red to white, or vise versa to draw the board
    if color == RED_COLOR:
        return WHITE_COLOR
    else:
        return RED_COLOR


def draw_board():  # draw the squares in alternating color
    color = WHITE_COLOR
    for i in range(BOARD_HEIGHT):
        color = alternate_white_red(color)
        for j in range(BOARD_WIDTH):
            color = alternate_white_red(color)
            square = pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE + Y_OFFSET, SQUARE_SIZE, SQUARE_SIZE)
            piece = board[i][j]
            if piece != None and piece.is_highlighted:  # if piece is highlighted, highlight the square
                pygame.draw.rect(window, HIGHLIGHT_COLOR, square)
            else:
                pygame.draw.rect(window, color, square)


def draw_captured_pieces():
    for player in players:
        for i in range(len(player.dead_pieces)):
            draw_x, draw_y = (i * SQUARE_SIZE / 2) + SQUARE_SIZE * .25, Y_OFFSET - SQUARE_SIZE * 1.25
            if player.color == PieceColor.BLACK:  # black pieces start lower down
                draw_y += (BOARD_HEIGHT * SQUARE_SIZE) + SQUARE_SIZE * 2
            if i >= BOARD_WIDTH:  # draw pieces on the second row if there are too many
                draw_y -= SQUARE_SIZE * 3 / 4
                draw_x -= (BOARD_WIDTH * SQUARE_SIZE / 2)
            window.blit(get_image(player.dead_pieces[i]), (draw_x, draw_y))



def draw_player_pieces(player):  # draw a player's pieces
    for piece in player.pieces:
        piece_image = get_image(piece)
        window.blit(piece_image, (piece.loc_x * SQUARE_SIZE, piece.loc_y * SQUARE_SIZE + Y_OFFSET))

    highlighted_piece = get_highlighted_piece()  # draw target squares for highlighted piece
    if highlighted_piece is not None:
        for square in highlighted_piece.available_squares:
            pygame.draw.circle(window, HIGHLIGHT_COLOR, (
                square[0] * SQUARE_SIZE + SQUARE_SIZE / 2, square[1] * SQUARE_SIZE + SQUARE_SIZE / 2 + Y_OFFSET),
                               SQUARE_SIZE / 6)


def get_image(piece):
    if piece.spriteLoc in image_cache:  # load sprite from cache
        piece_image = image_cache[piece.spriteLoc]
    else:
        piece_sprite = pygame.image.load(piece.spriteLoc)  # load sprite
        sprite_scalar = SQUARE_SIZE / max(piece_sprite.get_width(),
                                          piece_sprite.get_height())  # get scalar to maintain aspect ratio
        piece_image = pygame.transform.smoothscale(piece_sprite, (
            piece_sprite.get_width() * sprite_scalar, piece_sprite.get_height() * sprite_scalar))
        image_cache[piece.spriteLoc] = piece_image  # add created sprite to cache
    return piece_image


def calculate_squares_all_pieces():
    for player in players:
        for piece in player.pieces:
            piece.check_squares(board)


def draw_stat_panels():
    for player in players:
        draw_x, draw_y = WINDOW_WIDTH - 500, Y_OFFSET - 100
        text_color = BLACK_COLOR
        if player.color == PieceColor.BLACK: # draw lower down and switch text color
            draw_y += (BOARD_HEIGHT * SQUARE_SIZE) + 110
            text_color = WHITE_COLOR
        point_total = 0
        for piece in player.dead_pieces: # add up point values
            point_total += piece.value
        text = font.render(f'Points: {point_total}', True, text_color)
        window.blit(text, (draw_x, draw_y))


def draw():  # combines all draw functions
    window.fill((128, 128, 128))
    draw_board()
    draw_player_pieces(white_player)
    draw_player_pieces(black_player)
    draw_captured_pieces()
    draw_stat_panels()
    pygame.display.update()


def clear_highlights():
    for player in players:
        for piece in player.pieces:
            piece.remove_highlight()


def get_highlighted_piece():
    for player in players:
        for piece in player.pieces:
            if piece.is_highlighted:
                return piece
    return None


def switch_player_turn():
    global player_turn
    if player_turn == PieceColor.WHITE:
        player_turn = PieceColor.BLACK
    else:
        player_turn = PieceColor.WHITE


def handle_click(click_position):  # is run every time a click event is triggered
    square_x = math.floor(click_position[0] / SQUARE_SIZE)  # convert event coordinates to board squares
    square_y = math.floor((click_position[1] - Y_OFFSET) / SQUARE_SIZE)
    if Y_OFFSET < click_position[1] < (Y_OFFSET + BOARD_HEIGHT * SQUARE_SIZE):  # if the click was on the board
        clicked_piece = board[square_y][square_x]  # get the piece at the clicked location
        if clicked_piece is not None and clicked_piece.color is player_turn:  # clicked on playing color's piece
            clear_highlights()
            clicked_piece.add_highlight()
        else:
            highlighted_piece = get_highlighted_piece()
            if highlighted_piece is not None:  # a piece has been highlighted
                for square in highlighted_piece.available_squares:
                    if square == [square_x, square_y]:  # clicked square is a target
                        if isinstance(highlighted_piece, Pawn):  # keep track of pawn double moves
                            highlighted_piece.move_count += 1
                        board[highlighted_piece.loc_y][highlighted_piece.loc_x] = None

                        # capture piece
                        if board[square_y][square_x] is not None:
                            if (player_turn == PieceColor.WHITE):
                                black_player.remove_piece(board[square_y][square_x])
                            else:
                                white_player.remove_piece(board[square_y][square_x])
                        board[square_y][square_x] = None

                        board[square_y][square_x] = highlighted_piece
                        highlighted_piece.set_loc(square_x, square_y)  # move piece to clicked square
                        calculate_squares_all_pieces()
                        switch_player_turn()
            clear_highlights()
    else:
        clear_highlights()
    draw()


def main():
    FPS_clock = pygame.time.Clock()
    is_running = True
    read_config()
    calculate_squares_all_pieces()
    draw()
    while is_running:
        FPS_clock.tick(FPS_LIMIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_click(event.pos)

    pygame.quit()


if __name__ == "__main__":
    main();
