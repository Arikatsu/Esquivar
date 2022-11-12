from constants import Constants
import pygame

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = Constants.screen_width
        
    # def update(self):
