import pygame

import pygame.display
import pygame.image

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 720, 720
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Battlefield Chess")
FPS_LIMIT = 60
BOARD_WIDTH, BOARD_HEIGHT = 22, 12
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
board = [[]]

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
    for row in board_config:
        if len(row) == 0:
            continue
        else:
            for cell in row:
                piece_color = cell[0]
                piece_type = cell[1]


def alternate_color(color):  # swap the color from black to white, or vise versa
    if color == BLACK_COLOR:
        return WHITE_COLOR
    else:
        return BLACK_COLOR


def draw_board():
    cell_size = WINDOW_WIDTH / BOARD_WIDTH
    color = WHITE_COLOR
    y_offset = (WINDOW_HEIGHT - cell_size * BOARD_HEIGHT) // 2
    for i in range(BOARD_HEIGHT):
        color = alternate_color(color)
        for j in range(BOARD_WIDTH):
            color = alternate_color(color)
            cell = pygame.Rect(j * cell_size, i * cell_size + y_offset, cell_size, cell_size)
            pygame.draw.rect(window, color, cell)
    pygame.display.update()



def main():
    FPS_clock = pygame.time.Clock()
    is_running = True
    while is_running:
        window.fill((128, 128, 128))
        FPS_clock.tick(FPS_LIMIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        draw_board()
    pygame.quit()


if __name__ == "__main__":
    main();
