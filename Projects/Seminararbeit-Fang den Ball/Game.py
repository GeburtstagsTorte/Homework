import pygame
from pygame import gfxdraw
from random import randint
from Constants import Constants as C


class Game:

    game_lost = False
    click_event = True

    def __init__(self, time, time_factor, ball_color, ball_radius,
                 grid_size, lives, surface):
        self.time = time
        self.ball_color = ball_color
        self.ball_radius = ball_radius
        self.grid_size = grid_size
        self.time_factor = time_factor
        self.surface = surface

        x = randint(ball_radius, grid_size[0] - ball_radius)
        y = randint(ball_radius, grid_size[1] - ball_radius - C.ui_height)
        self.ball = Ball(ball_color, ball_radius, x, y)

        self.n = 0
        self.score = 0
        self.temp_score = 0
        self.lives = lives
        self.restart_button = C.initialize_restart_button(surface=self.surface)

    def render(self, surface):
        self.ball.render(surface)
        self.render_user_interface(surface)

        if self.game_lost:
            font = pygame.font.SysFont(C.font, C.font_lost_size)
            txt = font.render("You lost! Your score is " + str(self.score),
                              True, C.text_color)
            txt_rect = txt.get_rect(center=C.lost_pos)
            surface.blit(txt, txt_rect)

            self.restart_button.render()

    def update(self):

        if self.lives <= 0:
            self.game_lost = True
        else:
            self.n += 1

            if self.n % int(self.time) == 0:
                self.ball.x = randint(self.ball.radius, self.grid_size[0] -
                                      self.ball.radius)
                self.ball.y = randint(self.ball.radius, self.grid_size[1] -
                                      self.ball.radius - C.ui_py)
                self.n = 0

                if self.click_event:
                    self.lives -= 1

                self.click_event = True
                self.time *= self.time_factor

                if self.time < 1:
                    self.time = 1

            if self.ball.collide() and self.click_event:
                self.score += int(1000*(1/self.time))
                self.click_event = False

    def render_user_interface(self, surface):
        pygame.draw.line(surface, C.ui_color, [0, C.ui_height],
                         [C.width, C.ui_height])

        font = pygame.font.SysFont(C.font, C.font_size)
        txt_score = font.render("score: " + str(self.score), True,
                                C.text_color)
        txt_lives = font.render("lives: " + str(self.lives), True,
                                C.text_color)
        surface.blit(txt_score, C.score_pos)
        surface.blit(txt_lives, C.lives_pos)


class Ball:

    def __init__(self, color, radius, x, y):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y

    def render(self, surface):
        pygame.gfxdraw.circle(surface, self.x, self.y, self.radius,
                              self.color)

    def collide(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if (mouse_x - self.x)**2 + (mouse_y - self.y)**2 <= self.radius**2:
            return True
        return False
