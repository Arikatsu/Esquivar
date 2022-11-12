from constants import Constants

class KeyEvents: 
    def inverse_gravity(player, platform):
        if player.gravity < 0:
            player.gravity = Constants.gravity
        else:
            player.gravity = -Constants.gravity