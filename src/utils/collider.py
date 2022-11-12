import pygame
from constants import Constants

# Check for player collission with platforms
def check_collision(player, platformBottom, platformTop):
    if player.rect.colliderect(platformBottom.rect):
        player.rect.bottom = platformBottom.rect.top
    if player.rect.colliderect(platformTop.rect):
        player.rect.top = platformTop.rect.bottom