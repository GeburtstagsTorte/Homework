from pygame import image


class Constants:

    A, D = False, False
    SPACE = False

    WIDTH = 1000
    HEIGHT = 600

    player_size = WIDTH // 15
    alien_size = WIDTH // 20
    bullet_size = WIDTH // 15

    player_image = image.load("res/player.gif")
    alien_image = image.load("res/alien.png")
    bullet_image = image.load("res/bullet1.png")

    wave_size = 5
    counter = 0
