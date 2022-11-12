import pygame
import logging
from constants import Constants

class Player(pygame.sprite.Sprite):
    def __init__(self, canvas, position):
        self.canvas = canvas
        self.position = position
        self.velocity = 0
        self.gravity = Constants.gravity
        self.size = 50

    def draw(self):
        pygame.draw.rect(self.canvas, (0, 0, 20), (self.position[0], self.position[1], self.size, self.size))

    def move(self):
        self.velocity += self.gravity
        self.position[1] += self.velocity
        if self.position[1] > Constants.screen_height - self.size:
            self.position[1] = Constants.screen_height - self.size
            self.velocity = 0

    def jump(self):
        self.velocity = -10