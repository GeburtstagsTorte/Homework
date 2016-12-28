from Player import Player
from Aliens import Alien, MotherShip
from Constants import Constants
from Bullet import Bullet
from pygame import Rect


class Entities:
    player = None
    aliens = []
    player_bullet = []
    mother_ship = None
    alien_wave_counter = 0
    mother_ship_counter = 0

    def __init__(self):
        Entities.player = Player(
            [Constants.WIDTH // 2 - Constants.player_size // 2, Constants.HEIGHT - Constants.player_size - 10,
             Constants.player_size, Constants.player_size], [0, 75, 100, 25], Constants.player_image)
        # [from x move:, from y move:, size of the object on x, height of the object on y] for collision boxes

    @staticmethod
    def render(game_display):
        Entities.player.render(game_display)
        for alien in range(len(Entities.aliens)):
            Entities.aliens[alien].render(game_display)
        # if Constants.SPACE:
            # Entities.player_shoot_bullet(Entities.player, game_display)
        for bullet in Entities.player_bullet:
            bullet.render(game_display)
        if Entities.mother_ship:
            Entities.mother_ship.render(game_display)

    @staticmethod
    def update():
        if Constants.counter == 200:
            Entities.create_alien_wave(Constants.wave_size)
            Constants.counter = 0
            Entities.alien_wave_counter += 1
            """if Entities.alien_wave_counter > 5:
                Entities.create_mother_ship()
                Entities.alien_wave_counter = 0
                Entities.mother_ship_counter += 1"""

        Entities.player.update()

        for i in range(len(Entities.aliens)):
            Entities.aliens[i].update()

        for alien in Entities.aliens:
            if alien.pos_rect[0] >= Constants.WIDTH - Constants.alien_size or alien.pos_rect[0] <= 0:
                for j in Entities.aliens:
                    j.pos_rect[1] += Constants.alien_size // 2

        for bullet_id in range(len(Entities.player_bullet)):
            try:
                Entities.player_bullet[bullet_id].update()
                Entities.check_bullet_collision(bullet_id)
            except IndexError:
                pass

        if Entities.mother_ship:
            Entities.mother_ship.update()

    @staticmethod
    def player_shoot_bullet(player):
        Entities.player_bullet.append(Bullet(
            [player.draw_rect[0], player.draw_rect[1] - Constants.player_size,
             Constants.bullet_size, Constants.bullet_size], [45, 50, 10, 50], Constants.bullet_image))

    @staticmethod
    def create_alien_wave(n):
        for i in range(n):
            Entities.aliens.append(
                Alien([Constants.WIDTH // 2 - Constants.alien_size // 2 - Constants.alien_size * i,
                       Constants.HEIGHT // 18, Constants.alien_size, Constants.alien_size],
                      [0, 10, 100, 10], Constants.alien_image))

    @staticmethod
    def create_mother_ship():
        Entities.mother_ship = MotherShip([Constants.WIDTH // 2 - Constants.mother_ship_size // 2,
                                           Constants.HEIGHT // 20, Constants.mother_ship_size,
                                           Constants.mother_ship_size],
                                          [0, 10, 100, 10], Constants.death_star)

    @staticmethod
    def check_bullet_collision(bullet_id):
        for i in range(len(Entities.aliens)):
            if Entities.player_bullet[bullet_id].get_true_collision().colliderect(Entities.aliens[i].get_true_collision()):
                del Entities.player_bullet[bullet_id]
                del Entities.aliens[i]
                return True

        return False
