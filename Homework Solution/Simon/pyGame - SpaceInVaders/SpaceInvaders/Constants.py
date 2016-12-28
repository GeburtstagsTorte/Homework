from pygame import image


class Constants:

    A, D = False, False
    # SPACE = False

    WIDTH = 1000
    HEIGHT = 600

    player_size = WIDTH // 15
    alien_size = WIDTH // 20
    bullet_size = WIDTH // 15
    mother_ship_size = WIDTH // 10

    player_image = image.load("res/player.gif")
    alien_image = image.load("res/alien.png")
    bullet_image = image.load("res/bullet_red1.png")
    bomb_image = image.load("res/seism_bomb.png")
    death_star = image.load("res/deathstar.png")

    wave_size = 5
    counter = 0
