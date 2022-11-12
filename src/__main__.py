import pygame
import logging
from constants import Constants


def main():
    pygame.init()

    canvas = pygame.display.set_mode((800, 500))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Esquivar")
    exit = False

    while not exit:
        clock.tick(60)

        canvas.fill(Constants.background_color)
        pygame.draw.rect(canvas, (0, 0, 20), (Constants.position[0], Constants.position[1], 50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()

if __name__ == "__main__":
    main()
