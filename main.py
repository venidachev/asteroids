import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0 # delta time

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1_000


if __name__ == "__main__":
    main()