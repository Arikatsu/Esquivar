import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, gravity, height, width, color, pos_x, pos_y):
        super().__init__()
        self.gravity = gravity
        self.image = pygame.Surface((height, width))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def set_player_gravity(self):
        self.rect.bottom += self.gravity