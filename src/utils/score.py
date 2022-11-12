from constants import Constants

def score(points, game_speed, font_bold, canvas):
    points += 1
    if points % 100 == 0:
        game_speed += 1

    text = font_bold.render("Score: " + str(points), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (Constants.screen_width - 100, 30)
    canvas.blit(text, text_rect)
    return points, game_speed