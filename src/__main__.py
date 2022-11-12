import pygame, os
from player import Player
from constants import Constants
from platforms import Platforms
from utils.collider import check_collision

def main():
    pygame.init()

    # create screen
    canvas = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
    clock = pygame.time.Clock()

    pygame.display.set_caption(Constants.screen_title)

    # PLayer
    player = Player(Constants.gravity, Constants.height, Constants.width, Constants.color, Constants.position[0], Constants.position[1])
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # Background
    bg = pygame.image.load("assets/gfx/background.jpg")
    bg = pygame.transform.scale(bg, (Constants.screen_width, Constants.screen_height))

    # Platforms
    platformTop = Platforms(Constants.screen_width, 120, (0, 0, 0), Constants.screen_width / 2, 0)
    platformBottom = Platforms(Constants.screen_width, 120, (0, 0, 0), Constants.screen_width / 2, Constants.screen_height)
    platform_group = pygame.sprite.Group()
    platform_group.add(platformTop)
    platform_group.add(platformBottom)

    exit = False

    # Game loop
    while not exit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        canvas.blit(bg, (0, 0))
        player_group.draw(canvas)
        platform_group.draw(canvas)

        Player.set_player_gravity(player)

        check_collision(player, platformBottom, platformTop)

        pygame.display.flip()
        
if __name__ == "__main__":
    main()
