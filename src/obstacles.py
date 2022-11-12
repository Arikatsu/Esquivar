from constants import Constants
import pygame
import random

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((random.randint(60, 200), random.randint(60, 375)), pygame.SRCALPHA, 32)
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = Constants.screen_width
        self.rect.y = random.randint(50, 400)

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()