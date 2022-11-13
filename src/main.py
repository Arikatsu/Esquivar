import pygame, os
from player import Player
from constants import Constants
from platforms import Platforms
from obstacles import Obstacles
from utils.collider import check_collision
from utils.controls import KeyEvents
from utils.score import score
from utils.particles import Particles

death_count = 0
points = Constants.initial_score

def game():
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

    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 50)
    player_particles = Particles()

    # Game
    global points
    global death_count
    game_speed = Constants.initial_game_speed
    obstacles = []
    game_paused = True

    # Platforms
    platformTop = Platforms(Constants.screen_width, 120, (0, 0, 0), Constants.screen_width / 2, 0)
    platformBottom = Platforms(Constants.screen_width, 120, (0, 0, 0), Constants.screen_width / 2, Constants.screen_height)
    platform_group = pygame.sprite.Group()
    platform_group.add(platformTop)
    platform_group.add(platformBottom)

    global exit
    exit = False

    # Game loop
    while not exit:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN):
                KeyEvents.inverse_gravity(player, platformTop)

            if event.type == PARTICLE_EVENT:
                player_particles.add_particle(player)

        canvas.blit(bg, (0, 0))
        player_group.draw(canvas)

        platform_group.draw(canvas)

        while game_paused:
            canvas.fill((0, 0, 0))
            text = font_bold.render("Press any key to start", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (Constants.screen_width / 2, Constants.screen_height / 2)
            canvas.blit(text, text_rect)
            
            if death_count > 0:
                score_text = font_regular.render("Score: " + str(points), True, (255, 255, 255))
                score_text_rect = score_text.get_rect()
                score_text_rect.center = (Constants.screen_width / 2, Constants.screen_height / 2 + 50)
                canvas.blit(score_text, score_text_rect)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_paused = False
                    exit = True
                if event.type == pygame.KEYDOWN:
                    game_paused = False
                    points = 0

        Player.set_player_gravity(player)
        points, game_speed, player.gravity = score(points, game_speed, player.gravity, font_bold, canvas)

        if len(obstacles) == 0:
            obstacles.append(Obstacles())

        for obstacle in obstacles:
            obstacle.update(game_speed, obstacles)
            canvas.blit(obstacle.image, obstacle.rect)
            if player.rect.colliderect(obstacle.rect):
                death_count += 1
                game()

        player_particles.emit(canvas)
        pygame.display.update()
        check_collision(player, platformBottom, platformTop)

pygame.quit()
        
if __name__ == "__main__":
    game()
