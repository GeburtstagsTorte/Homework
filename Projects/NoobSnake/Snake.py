import pygame
from Constants import Constants as C
from Button import Button as Btn
from random import randrange
from datetime import datetime


class Segment:

    def __init__(self, x, y, color, surface, length=C.length, height=C.length):
        self.x = x
        self.y = y
        self.color = color
        self.surface = surface
        self.length = length
        self.height = height

    def render(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.length, self.height))

    def update(self):
        pass


class Food:

    def __init__(self, x, y, surface, color, length=C.length, height=C.length):
        self.x = x
        self.y = y
        self.surface = surface
        self.color = color
        self.length = length
        self.height = height

    def render(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.length, self.height))


class Objects:

    segments = []
    # food = object
    food_x = randrange(0, C.width - C.length, C.length)
    food_y = randrange(0, C.height - C.length - C.ui_height, C.length)
    score = 0
    game_lost = False
    log = True

    btn_restart = object
    btn_pause = object
    btn_scores = object
    btn_exit = object
    btn_settings = object
    btn_start = object

    def __init__(self, game_display):
        Objects.add_segment(game_display, C.width // 2, C.height // 2)
        Objects.initialize_buttons(game_display)

    @staticmethod
    def render_game(game_display, mouse_click):
        Food(Objects.food_x, Objects.food_y, game_display, C.red).render()

        for i in range(len(Objects.segments)):
            Objects.segments[i].render()

        Objects.render_grid(game_display)
        Objects.render_ui(game_display)
        Objects.render_score(game_display)
        Objects.handle_restart_button(game_display, mouse_click)
        Objects.handle_pause_button(mouse_click)

        if Objects.game_lost:
            Objects.render_lose_screen(game_display)

    @staticmethod
    def render_menu(game_display, mouse_click):
        font = pygame.font.SysFont(C.menu_font, C.menu_size)
        txt = font.render(C.menu_text, True, C.menu_color)
        txt_rect = txt.get_rect(center=(C.width//2, C.menu_height))
        game_display.blit(txt, txt_rect)

        Objects.handle_start_button(mouse_click)
        Objects.handle_scores_button(mouse_click)
        Objects.handle_settings_button(mouse_click)

    @staticmethod
    def render_grid(surface):
        for i in range(C.length, C.width, C.length):
            pygame.draw.line(surface, C.grid_color, (i, 0), (i, C.height - C.ui_height))
        for i in range(C.length, C.height - C.ui_height, C.length):
            pygame.draw.line(surface, C.grid_color, (0, i), (C.width, i))

    @staticmethod
    def render_ui(surface):
        surface.blit(C.ui_background, (0, C.height - C.ui_height))
        snake_rect = C.ui_snake.get_rect()
        surface.blit(C.ui_snake, ((C.width - snake_rect[2]) // 2, C.height - C.ui_height + 10))

    @staticmethod
    def render_score(surface):
        font = pygame.font.SysFont(C.score_font, C.score_size)
        txt = font.render(C.score_text + str(Objects.score), True, C.score_color)
        surface.blit(txt, C.score_pos)

    @staticmethod
    def render_lose_screen(surface):
        image_rect = C.lose_screen.get_rect()
        surface.blit(C.lose_screen, ((C.width - image_rect[2]) // 2, (C.height - C.ui_height - image_rect[3])//2))

    @staticmethod
    def update(game_display):

        for i in range(len(Objects.segments) - 1, 0, -1):
            if C.speed != 0:
                Objects.segments[i].x = Objects.segments[i - 1].x
                Objects.segments[i].y = Objects.segments[i - 1].y
            else:
                break

        Objects.segments[0].x += C.dir[0] * C.speed
        Objects.segments[0].y += C.dir[1] * C.speed

        if Objects.check_border() or Objects.check_if_intersect():
            C.speed = 0
            Objects.game_lost = True

        Objects.check_food_collision(game_display)

        if Objects.game_lost and Objects.log:
            Objects.track_score()

    @staticmethod
    def add_segment(game_display, x, y):
        Objects.segments.append(Segment(x, y, C.segment_color, game_display))

    @staticmethod
    def handle_keys(event):
        if event.type == pygame.KEYDOWN:
            if event.key == 119 or event.key == 273:
                # w
                C.dir = (0, -1)

            if event.key == 97 or event.key == 276:
                # a
                C.dir = (-1, 0)

            if event.key == 115 or event.key == 274:
                # s
                C.dir = (0, 1)

            if event.key == 100 or event.key == 275:
                # d
                C.dir = (1, 0)

    @staticmethod
    def check_border():
        if 0 > Objects.segments[0].x or Objects.segments[0].x > (C.width - C.length) or \
                        0 > Objects.segments[0].y or Objects.segments[0].y > (C.height - C.length - C.ui_height):
            return True
        return False

    @staticmethod
    def check_food_collision(game_display):
        for segment in Objects.segments:
            if segment.x == Objects.food_x and segment.y == Objects.food_y:
                for i in range(C.addition_rate):
                    Objects.add_segment(game_display, Objects.segments[len(Objects.segments)-1].x,
                                        Objects.segments[len(Objects.segments)-1].y)

                Objects.food_x = randrange(0, C.width - C.length - C.ui_height, C.length)
                Objects.food_y = randrange(0, C.height - C.length - C.ui_height, C.length)
                Objects.score += C.addition_rate

    @staticmethod
    def check_if_intersect():
        for i in range(1, len(Objects.segments)):
            if Objects.segments[0].x == Objects.segments[i].x and \
                            Objects.segments[0].y == Objects.segments[i].y:

                Objects.segments[0].color = C.blue
                Objects.segments[i].color = C.blue
                return True
        return False

    @staticmethod
    def track_score():
        Objects.log = False
        time = datetime.now()

        if Objects.score > 0:
            with open("score.txt", "a") as file:
                file.write(C.player_name + " " + str(Objects.score) + " " + str(time))
                file.write("\n")

    @staticmethod
    def initialize_buttons(game_display):
        Objects.btn_restart = Btn(game_display, (0, 0), C.btn_width, C.btn_height, C.btn_color, C.btn_restart_txt,
                                  C.btn_size, C.btn_font_color, C.btn_font, mod=2, border=C.btn_font_color, extend=True)
        Objects.btn_scores = Btn(game_display, (0, 0), C.btn_menu_width, C.btn_menu_height, C.btn_color,
                                 C.btn_scores_txt, C.btn_size, C.btn_font_color, C.btn_font, mod=2,
                                 border=C.btn_font_color, extend=True)
        Objects.btn_exit = Btn(game_display, (0, 0), C.btn_menu_width, C.btn_menu_height, C.btn_color, C.btn_exit_txt,
                               C.btn_size, C.btn_font_color, C.btn_font, mod=2, border=C.btn_font_color, extend=True)
        Objects.btn_settings = Btn(game_display, (0, 0), C.btn_menu_width, C.btn_menu_height, C.btn_color,
                                   C.btn_settings_txt, C.btn_size, C.btn_font_color, C.btn_font, mod=2,
                                   border=C.btn_font_color, extend=True)
        Objects.btn_pause = Btn(game_display, (0, 0), C.btn_width, C.btn_height, C.btn_color, C.btn_pause_txt,
                                C.btn_size, C.btn_font_color, C.btn_font, mod=2, border=C.btn_font_color, extend=True)
        Objects.btn_start = Btn(game_display, (0, 0), C.btn_menu_width, C.btn_menu_height, C.btn_color, C.btn_start_txt,
                                C.btn_size, C.btn_font_color, C.btn_font, mod=2, border=C.btn_font_color, extend=True)

    @staticmethod
    def handle_restart_button(game_display, mouse_click):

        Objects.btn_restart.pos = C.btn_restart_pos
        Objects.btn_restart.render()

        if Objects.btn_restart.clicked(mouse_click):
            Objects.segments = []
            Objects.add_segment(game_display, C.width // 2, C.height // 2)
            # food = object
            Objects.food_x = randrange(0, C.width - C.length, C.length)
            Objects.food_y = randrange(0, C.height - C.length - C.ui_height, C.length)
            Objects.score = 0
            C.speed = C.magnitude
            C.dir = (0, -1)
            Objects.game_lost = False
            Objects.log = True

    @staticmethod
    def handle_pause_button(mouse_click):

        Objects.btn_pause.pos = C.btn_pause_pos
        Objects.btn_pause.render()

        if Objects.btn_pause.clicked(mouse_click):
            if Objects.btn_pause.text == C.btn_pause_txt:
                C.speed = 0
                Objects.btn_pause.text = C.btn_pause_txt2
            else:

                C.speed = C.magnitude
                Objects.btn_pause.text = C.btn_pause_txt

    @staticmethod
    def handle_start_button(mouse_click):

        Objects.btn_start.pos = C.btn_start_pos
        Objects.btn_start.render()

        if Objects.btn_start.clicked(mouse_click):
            return True

    @staticmethod
    def handle_scores_button(mouse_click):

        Objects.btn_scores.pos = C.btn_scores_pos
        Objects.btn_scores.render()

        if Objects.btn_scores.clicked(mouse_click):
            pass

    @staticmethod
    def handle_settings_button(mouse_click):

        Objects.btn_settings.pos = C.btn_settings_pos
        Objects.btn_settings.render()

        if Objects.btn_settings.clicked(mouse_click):
            pass

    @staticmethod
    def handle_exit_button(mouse_click):

        Objects.btn_exit.pos = C.btn_exit_pos
        Objects.btn_exit.render()

        if Objects.btn_exit.clicked(mouse_click):
            return True
