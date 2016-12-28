from pygame import image


class Constants:

    A, D = False, False         # why doesnt it take in keyboard input tho?
    SPACE = False

    WIDTH = 1000
    HEIGHT = 600

    player_size = WIDTH // 15
    alien_size = WIDTH // 15
    bullet_size = WIDTH // 15

    player_image = image.load("res/player.gif")
    alien_image = image.load("res/alien.png")
    bullet_image = image.load("res/bullet1.png")

    wave_size = 5
