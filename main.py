import pygame

import pygame.display
import pygame.image

from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from peice_color import PieceColor
from player import Player
from queen import Queen
from rook import Rook

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 720, 720
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Battlefield Chess")
FPS_LIMIT = 60
BOARD_WIDTH, BOARD_HEIGHT = 22, 12
CELL_SIZE = min(WINDOW_WIDTH, WINDOW_HEIGHT)/max(BOARD_WIDTH, BOARD_HEIGHT)
Y_OFFSET = (WINDOW_HEIGHT - CELL_SIZE * BOARD_HEIGHT) // 2
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
board = [[]]

# initiate players
white_player = Player()
black_player = Player()

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
    for i in range(len(board_config)):
        if len(board_config[i]) == 0:
            continue
        else:
            for j in range(len(board_config[i])):
                piece_color_char = board_config[i][j][0]
                piece_type_char = board_config[i][j][1]
                piece_color = None
                newPiece = None

                if piece_color_char == 'w': #get the piece color
                    piece_color = PieceColor.WHITE
                elif piece_color_char == 'b':
                    piece_color = PieceColor.BLACK

                match piece_type_char: #get the piece type and instantiate it
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
                #add piece to correct player
                if piece_color == PieceColor.WHITE:
                    white_player.add_piece(newPiece)
                elif piece_color == PieceColor.BLACK:
                    black_player.add_piece(newPiece)


def alternate_color(color):  # swap the color from black to white, or vise versa
    if color == BLACK_COLOR:
        return WHITE_COLOR
    else:
        return BLACK_COLOR


def draw_board():
    color = WHITE_COLOR
    for i in range(BOARD_HEIGHT):
        color = alternate_color(color)
        for j in range(BOARD_WIDTH):
            color = alternate_color(color)
            cell = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE + Y_OFFSET, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, color, cell)

def draw():
    draw_board()
    for piece in white_player.pieces:
        piece_sprite = pygame.image.load(piece.spriteLoc)
        piece_image = pygame.transform.scale(piece_sprite, (CELL_SIZE * .9, CELL_SIZE * .9))
        window.blit(piece_image, (piece.locX * CELL_SIZE, piece.locY * CELL_SIZE + Y_OFFSET))
    for piece in black_player.pieces:
        piece_sprite = pygame.image.load(piece.spriteLoc)
        piece_image = pygame.transform.scale(piece_sprite, (CELL_SIZE * .9, CELL_SIZE * .9))
        window.blit(piece_image, (piece.locX * CELL_SIZE, piece.locY * CELL_SIZE + Y_OFFSET))
    pygame.display.update()


def main():
    FPS_clock = pygame.time.Clock()
    is_running = True
    read_config()
    draw()
    while is_running:
        window.fill((128, 128, 128))
        FPS_clock.tick(FPS_LIMIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

    pygame.quit()


if __name__ == "__main__":
    main();
