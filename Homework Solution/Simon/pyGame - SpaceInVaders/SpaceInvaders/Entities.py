from Player import Player
from Aliens import Alien
from Constants import Constants
from Bullet import Bullet


class Entities:
    player = None
    aliens = []
    player_bullet = None

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
        if Constants.SPACE:
            Entities.player_shoot_bullet(Entities.player, game_display)
        if Entities.player_bullet:
            Entities.player_bullet.render(game_display)

    @staticmethod
    def update():
        if len(Entities.aliens) < 5:
            Entities.create_alien_wave_5()

        Entities.player.update()
        for i in range(len(Entities.aliens)):
            Entities.aliens[i].update()
        for alien in Entities.aliens:
            if alien.pos_rect[0] >= Constants.WIDTH - Constants.alien_size or alien.pos_rect[0] <= 0:
                for j in Entities.aliens:
                    j.pos_rect[1] += Constants.alien_size // 2
        if Entities.player_bullet:
            Entities.player_bullet.update()
            Entities.check_bullet_collision()

    @staticmethod
    def player_shoot_bullet(player, game_display):
        Entities.player_bullet = Bullet(
            [player.draw_rect[0], player.draw_rect[1] - Constants.player_size,
             Constants.bullet_size, Constants.bullet_size], [40, 50, 20, 50], Constants.bullet_image)
        Entities.player_bullet.shoot_bullet(Entities.player_bullet, game_display)

    @staticmethod
    def create_alien_wave_5():  # as of yet loop doesnt work
        Entities.aliens = Alien(
            [Constants.WIDTH // 2 - Constants.alien_size // 2, Constants.alien_size,
             Constants.alien_size, Constants.alien_size], [0, 10, 100, 10], Constants.alien_image), Alien(
            [Constants.WIDTH // 2 - Constants.alien_size // 2 - Constants.alien_size, Constants.alien_size,
             Constants.alien_size, Constants.alien_size], [0, 10, 100, 10], Constants.alien_image), Alien(
            [Constants.WIDTH // 2 - Constants.alien_size // 2 - Constants.alien_size * 2, Constants.alien_size,
             Constants.alien_size, Constants.alien_size], [0, 10, 100, 10], Constants.alien_image), Alien(
            [Constants.WIDTH // 2 - Constants.alien_size // 2 - Constants.alien_size * 3, Constants.alien_size,
             Constants.alien_size, Constants.alien_size], [0, 10, 100, 10], Constants.alien_image), Alien(
            [Constants.WIDTH // 2 - Constants.alien_size // 2 - Constants.alien_size * 4, Constants.alien_size,
             Constants.alien_size, Constants.alien_size], [0, 10, 100, 10], Constants.alien_image)

    @staticmethod
    def check_bullet_collision():
        for i in range(len(Entities.aliens)):
            if Entities.player_bullet:
                if Entities.bullet_aliens_pos_x(i) and Entities.bullet_aliens_pos_y(i):
                    Entities.player_bullet = None
                    # Entities.aliens[i] = None            # this one fucks with me m888
                    """
                    so.. don't get me wrong :D I did multiple research attempts to solve this one and came to a
                    conclusion that i simply don't have enough knowledge about objects and classes. This probably has
                    smth to do with reference counts etc...
                    i tried to delete, remove, etc.
                    """

    @staticmethod
    def bullet_aliens_pos_x(i):
        for j in range(Entities.player_bullet.pos_rect[0] + Entities.player_bullet.collision_box[0],
                       Entities.player_bullet.pos_rect[0] + Entities.player_bullet.collision_box[0] +
                       Entities.player_bullet.collision_box[2]):
            if j in range(Entities.aliens[i].pos_rect[0] + Entities.aliens[i].collision_box[0],
                          Entities.aliens[i].pos_rect[0] + Entities.aliens[i].collision_box[0] +
                          Entities.aliens[i].collision_box[2]):
                return True

    @staticmethod
    def bullet_aliens_pos_y(i):
        for j in range(Entities.player_bullet.pos_rect[1] + Entities.player_bullet.collision_box[1],
                       Entities.player_bullet.pos_rect[1] + Entities.player_bullet.collision_box[1] +
                       Entities.player_bullet.collision_box[3]):
            if j in range(Entities.aliens[i].pos_rect[1] + Entities.aliens[i].collision_box[1],
                          Entities.aliens[i].pos_rect[1] + Entities.aliens[i].collision_box[1] +
                          Entities.aliens[i].collision_box[2] // 2):
                return True
