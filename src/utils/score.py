from constants import Constants

def score(points, game_speed, gravity, high_score, font_bold, canvas):
    points += 1
    if points % 500 == 0:
        game_speed += 1
        gravity += 1

    text = font_bold.render("Score: " + str(points), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (Constants.screen_width - 100, 30)
    canvas.blit(text, text_rect)
    high_score_text = font_bold.render("High Score: " + str(high_score), True, (255, 255, 255))
    high_score_text_rect = high_score_text.get_rect()
    high_score_text_rect.center = (120, 30)
    canvas.blit(high_score_text, high_score_text_rect)
    if points > high_score:
        high_score = points
    return points, game_speed, gravity, high_score