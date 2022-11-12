import pygame

# create platfroms on top and bottom of screen
class Platforms(pygame.sprite.Sprite):
    def __init__(self, width, height, color, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]