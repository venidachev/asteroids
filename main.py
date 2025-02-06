import pygame
from constants import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0 # delta time

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        pygame.display.update()
        dt = clock.tick(60) / 1_000


if __name__ == "__main__":
    main()