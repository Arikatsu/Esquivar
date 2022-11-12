import pygame, os
from player import Player
from constants import Constants
from platforms import Platforms
from obstacles import Obstacles
from utils.collider import check_collision
from utils.controls import KeyEvents
from utils.score import score

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

    # Visuals
    bg = pygame.image.load("assets/gfx/background.jpg")
    bg = pygame.transform.scale(bg, (Constants.screen_width, Constants.screen_height))

    font_regular = pygame.font.Font("assets/fonts/OverpassMono-Regular.ttf", 20)
    font_bold = pygame.font.Font("assets/fonts/OverpassMono-Bold.ttf", 20)

    points = Constants.initial_score
    game_speed = Constants.initial_game_speed
    obstacles = []

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
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    KeyEvents.inverse_gravity(player, platformTop)

        canvas.blit(bg, (0, 0))
        player_group.draw(canvas)
        platform_group.draw(canvas)

        Player.set_player_gravity(player)
        points, game_speed = score(points, game_speed, font_bold, canvas)

        if len(obstacles) == 0:
            obstacles.append(Obstacles())

        for obstacle in obstacles:
            obstacle.update(game_speed, obstacles)
            canvas.blit(obstacle.image, obstacle.rect)
            if player.rect.colliderect(obstacle.rect):
                pygame.draw.rect(canvas, (255, 0, 0), player.rect, 5)

        pygame.display.update()
        check_collision(player, platformBottom, platformTop)

        pygame.display.flip()
        
if __name__ == "__main__":
    main()
