from Player import Player
from Aliens import Alien, MotherShip
from Constants import Constants
from Bullet import Bullet, SeismBomb, AlienBullet
import pygame
from random import randint


class Entities:
    player = None
    aliens = []
    player_bullet = []
    alien_bullet = []
    mothership_bullet = []
    seism_bomb = []
    mother_ship = []
    alien_wave_counter = 0
    mother_ship_counter = 0
    won = 0

    def __init__(self):
        Entities.player = Player(
            [Constants.WIDTH // 2 - Constants.player_size // 2, Constants.HEIGHT - Constants.player_size - 10,
             Constants.player_size, Constants.player_size], [0, 75, 100, 25], Constants.player_image, 10)
        # [from x move:, from y move:, size of the object on x, height of the object on y] for collision boxes

    @staticmethod
    def handle_game():
        if Constants.counter == 240:
            Entities.create_alien_wave(Constants.wave_size)
            Constants.counter = 0
            Entities.alien_wave_counter += 1
            if Entities.alien_wave_counter == 5 and len(Entities.mother_ship) == 0:
                Entities.create_mother_ship(Constants.mother_ship_size, 10, Constants.star_destroyer, [20, 5, 60, 90])
                Entities.alien_wave_counter = 0
            elif Entities.mother_ship_counter == 3 and len(Entities.mother_ship) == 0:
                Entities.create_mother_ship(Constants.mother_ship_size * 1.5, 25, Constants.death_star,
                                            [0, 10, 100, 10])
                if len(Entities.mother_ship) < 1:
                    Entities.won = 1

            if len(Entities.mother_ship) > 0:
                Constants.wave_size = 5
            elif len(Entities.mother_ship) == 0:
                Constants.wave_size = 6

        if Constants.counter == 100:
            if len(Entities.aliens) > 1:
                for i in range(0, len(Entities.aliens) // 3):
                    rand_int = randint(0, len(Entities.aliens) - 1)
                    Entities.alien_shoot_bullet(rand_int)

        if Constants.counter == 200 and len(Entities.mother_ship) > 0:
            Entities.mothership_shoot_bullet(0)

    @staticmethod
    def render(game_display):
        if Constants.lost == 0 and Entities.won != 4:
            Entities.render_game(game_display)
        elif Constants.lost == 1:
            Entities.render_game(game_display)
            game_display.blit(Constants.game_over, [Constants.WIDTH // 4, Constants.HEIGHT // 3, 100, 100])
        elif Entities.won == 4:
            Entities.render_game(game_display)
            game_display.blit(Constants.game_won, [Constants.WIDTH // 30, Constants.WIDTH // 4, 100, 100])

    @staticmethod
    def render_game(game_display):
        Entities.player.render(game_display)

        for bullet in Entities.player_bullet:
            bullet.render(game_display)
        for bomb in Entities.seism_bomb:
            bomb.render(game_display)
        for alien_bullet in Entities.alien_bullet:
            alien_bullet.render(game_display)
        for mother_ship_bullet in Entities.mothership_bullet:
            mother_ship_bullet.render(game_display)

        for mother_id in range(len(Entities.mother_ship)):
            Entities.mother_ship[mother_id].render(game_display)
        for alien in range(len(Entities.aliens)):
            Entities.aliens[alien].render(game_display)

    @staticmethod
    def update():
        if Constants.lost == 0 and Entities.won != 4:
            Entities.handle_game()
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

            for bomb_id in range(len(Entities.seism_bomb)):
                try:
                    Entities.seism_bomb[bomb_id].update()
                    Entities.check_bomb_collision(bomb_id)
                except IndexError:
                    pass

            for alien_bullet_id in range(len(Entities.alien_bullet)):
                try:
                    Entities.alien_bullet[alien_bullet_id].update()
                    Entities.check_alien_bullet_collision(alien_bullet_id)
                except IndexError:
                    pass

            for mother_ship_bullet_id in range(len(Entities.mothership_bullet)):
                try:
                    Entities.mothership_bullet[mother_ship_bullet_id].update()
                    Entities.check_mother_ship_bullet_collision(mother_ship_bullet_id)
                except IndexError:
                    pass

            for mother_ship in range(len(Entities.mother_ship)):
                try:
                    Entities.mother_ship[mother_ship].update()
                    for bullet_id in range(len(Entities.player_bullet)):
                        for bomb_id in range(len(Entities.seism_bomb)):
                            Entities.check_deathstar_collision(bullet_id, bomb_id)
                except IndexError:
                    pass
        else:
            pass

    @staticmethod
    def player_shoot_bullet(player):
        Entities.player_bullet.append(Bullet(
            [player.draw_rect[0], player.draw_rect[1] - Constants.player_size,
             Constants.bullet_size, Constants.bullet_size], [45, 50, 10, 50], Constants.bullet_image))

    @staticmethod
    def alien_shoot_bullet(alien_id):
        Entities.alien_bullet.append(AlienBullet(
            [Entities.aliens[alien_id].pos_rect[0] + Constants.alien_size // 2,
             Entities.aliens[alien_id].pos_rect[1] + Constants.alien_size,
             Constants.alien_size, Constants.alien_size], [45, 50, 10, 50], Constants.bullet_image))

    @staticmethod
    def mothership_shoot_bullet(ship_id):
        Entities.mothership_bullet.append(AlienBullet(
            [Entities.mother_ship[ship_id].pos_rect[0],
             Entities.mother_ship[ship_id].pos_rect[1] + Constants.mother_ship_size,
             Constants.mother_ship_size, Constants.mother_ship_size], [45, 50, 10, 50], Constants.mother_ship_bullet))

    @staticmethod
    def player_shoot_seism_bomb(player):
        Entities.seism_bomb.append(SeismBomb(
            [player.draw_rect[0], player.draw_rect[1] - Constants.player_size,
             Constants.bullet_size, Constants.bullet_size], [35, 60, 30, 40], Constants.bomb_image))

    @staticmethod
    def create_alien_wave(n):
        for i in range(n):
            Entities.aliens.append(
                Alien([Constants.WIDTH // 2 - Constants.alien_size // 2 - Constants.alien_size * i,
                       Constants.HEIGHT // 10, Constants.alien_size, Constants.alien_size],
                      [0, 10, 100, 10], Constants.alien_image))

    @staticmethod
    def create_mother_ship(size, health, image, collision_box):
        Entities.mother_ship.append(MotherShip([Constants.WIDTH // 2 - size // 2, Constants.HEIGHT // 20, size, size],
                                               collision_box, image, health))

    @staticmethod
    def check_bullet_collision(bullet_id):
        for i in range(len(Entities.aliens)):
            if Entities.player_bullet[bullet_id].get_true_collision().colliderect(
                    Entities.aliens[i].get_true_collision()):
                del Entities.player_bullet[bullet_id]
                del Entities.aliens[i]
                return True
        if Entities.player_bullet[bullet_id].pos_rect[1] < - Constants.bullet_size:
            del Entities.player_bullet[bullet_id]

        return False

    @staticmethod
    def check_bomb_collision(bomb_id):
        for i in range(len(Entities.aliens)):
            if Entities.seism_bomb[bomb_id].get_true_collision().colliderect(
                    Entities.aliens[i].get_true_collision()):
                del Entities.seism_bomb[bomb_id]
                del Entities.aliens[i-1:i+1]
                return True
        if Entities.seism_bomb[bomb_id].pos_rect[1] < - Constants.bullet_size:
            del Entities.seism_bomb[bomb_id]

        return False

    @staticmethod
    def check_alien_bullet_collision(bullet_id):
        if Entities.alien_bullet[bullet_id].get_true_collision().colliderect(Entities.player.get_true_collision()):
            Entities.player.health -= 1
            del Entities.alien_bullet[bullet_id]
        elif Entities.alien_bullet[bullet_id].pos_rect[1] > Constants.HEIGHT:
            del Entities.alien_bullet[bullet_id]
        elif Entities.player.health < 1:
            Constants.lost = 1

    @staticmethod
    def check_mother_ship_bullet_collision(bullet_id):
        if Entities.mothership_bullet[bullet_id].get_true_collision().colliderect(Entities.player.get_true_collision()):
            Entities.player.health -= 3
            del Entities.mothership_bullet[bullet_id]
        elif Entities.mothership_bullet[bullet_id].pos_rect[1] > Constants.HEIGHT:
            del Entities.mothership_bullet[bullet_id]
        elif Entities.player.health < 1:
            Constants.lost = 1

    @staticmethod
    def check_deathstar_collision(bullet_id, bomb_id):
        for i in range(len(Entities.mother_ship)):
            if Entities.player_bullet[bullet_id].get_true_collision().colliderect(
                    Entities.mother_ship[i].get_true_collision()):
                del Entities.player_bullet[bullet_id]
                Entities.mother_ship[i].health -= 1
                print(Entities.mother_ship[i].health)
            elif Entities.seism_bomb[
                bomb_id].get_true_collision().colliderect(
                    Entities.mother_ship[i].get_true_collision()):
                del Entities.seism_bomb[bomb_id]
                Entities.mother_ship[i].health -= 3
                print(Entities.mother_ship[i].health)
            elif Entities.mother_ship[i].health < 1:
                Entities.alien_wave_counter = 0
                Entities.mother_ship_counter += 1
                Entities.won += 1
                del Entities.mother_ship[i]
                return True

        return False
