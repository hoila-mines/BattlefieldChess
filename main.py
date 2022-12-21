import pygame

import pygame.display
import pygame.image

SIZE = WIDTH, HEIGHT = 720, 720
window = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Battlefield Chess")
FPS_LIMIT = 60
BOARD_WIDTH, BOARD_HEIGHT = 22, 12


def calculate_cell_size():
    if window.get_size()[0] < window.get_size()[1]:
        return window.get_size()[0]/BOARD_WIDTH
    else:
        return window.get_size()[1]/BOARD_WIDTH

def calculate_offset():
    board_pixel_width = BOARD_WIDTH * calculate_cell_size()
    board_pixel_height = BOARD_HEIGHT * calculate_cell_size()
    xOffset = window.get_size()/2
    yOffset = window.get
def draw_board():
    cell_size = calculate_cell_size()
    color = (0, 0, 0)
    for i in range(BOARD_HEIGHT):
        if color == (0, 0, 0):
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        for j in range(BOARD_WIDTH):
            if color == (0, 0, 0):
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            cell = pygame.Rect(j*cell_size, i*cell_size, cell_size, cell_size)
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