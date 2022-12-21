import pygame

import pygame.display

SIZE = WIDTH, HEIGHT = 720, 720
WINDOW = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Battlefield Chess")
WINDOW.fill((128, 128, 128))
FPS_limit = 60

def main():
    FPS_clock = pygame.time.Clock()
    is_running = True
    while is_running:
        FPS_clock.tick(FPS_limit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main();