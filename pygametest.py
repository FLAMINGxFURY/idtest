import pygame, sys

pygame.init()

SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)

pygame.display.set_caption('It Works!')

CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)

while True:

    CLOCK.tick(FPS)
    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
