from pygame import image


class Constants:

    A, D = False, False
    lost = 0

    WIDTH = 1000
    HEIGHT = 600

    player_size = WIDTH // 15
    alien_size = WIDTH // 20
    bullet_size = WIDTH // 15
    mother_ship_size = WIDTH // 10

    player_image = image.load("res/player.gif")
    alien_image = image.load("res/alien.png")
    bullet_image = image.load("res/bullet_red1.png")
    bomb_image = image.load("res/rocket.png")
    death_star = image.load("res/deathstar.png")
    star_destroyer = image.load("res/stardestroyer.png")
    mother_ship_bullet = image.load("res/mother_ship_bullet.png")
    game_over = image.load("res/game_over.png")
    game_won = image.load("res/game_won.png")

    wave_size = 5
    counter = 0
