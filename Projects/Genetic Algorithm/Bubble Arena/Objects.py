import pygame
from random import randint
from Button import Button as Btn
from Constants import Constants as C
from Bubbles import Bubbles as Bbl
from Bubbles import Food


class Objects:

    btn_pause = object
    btn_restart = object
    bubbles = []
    bbl1 = []
    bbl2 = []
    bbl3 = []
    food = []
    n = 0
    time = 0

    def __init__(self):
        pass

    @staticmethod
    def init_objects(game_display):
        Objects.init_buttons(game_display)
        Objects.init_bubbles(C.quantity, C.q_bubble)

    @staticmethod
    def structure(game_display, width, height, color, proportion=0.8):
        pygame.draw.line(game_display, color, (0, int(proportion*height)), (width, int(proportion*height)))

    @staticmethod
    def init_buttons(game_display):
        """surface, pos, width, height, color=(120, 120, 120), text='', text_size=10, text_color=(0, 0, 0),
                 font='Arial', image=None, image2=None, mod=None, border=None, extend=False"""
        Objects.btn_pause = Btn(game_display, C.ps_pos, C.btn_width, C.btn_height, C.btn_color, C.ps_text,
                                C.btn_txt_size, C.btn_text_color, C.btn_font, mod=C.btn_mod, border=C.btn_border_color)
        Objects.btn_restart = Btn(game_display, C.rst_pos, C.btn_width, C.btn_height, C.btn_color, C.rst_text,
                                  C.btn_txt_size, C.btn_text_color, C.btn_font, mod=C.btn_mod, border=C.btn_border_color)

    @staticmethod
    def init_bubbles(quantity, q):

        for bubble in range(quantity // q):
            Objects.bubbles.append(Bbl(C.bbl1_radius, C.bbl1_speed, C.bbl1_color, C.bbl1_species))
            Objects.bbl1.append(Bbl(C.bbl1_radius, C.bbl1_speed, C.bbl1_color, C.bbl1_species))

        for bubble in range(quantity // q):
            Objects.bubbles.append(Bbl(C.bbl2_radius, C.bbl2_speed, C.bbl2_color, C.bbl1_species))
            Objects.bbl2.append(Bbl(C.bbl2_radius, C.bbl2_speed, C.bbl2_color, C.bbl1_species))

        for bubble in range(quantity // q):
            Objects.bubbles.append(Bbl(C.bbl3_radius, C.bbl3_speed, C.bbl3_color, C.bbl3_species))
            Objects.bbl3.append(Bbl(C.bbl3_radius, C.bbl3_speed, C.bbl3_color, C.bbl3_species))

    @staticmethod
    def update_bubbles():
        Objects.n += 1
        for bubble in Objects.bubbles:
            if Objects.time == C.year:
                bubble.age += 1
            elif Objects.time == C.hungry:
                bubble.hp -= C.default_decrease

            for food in Objects.food:
                if food.collide((bubble.x, bubble.y), bubble.radius):
                    bubble.hp += food.health
                    del Objects.food[Objects.food.index(food)]
            if bubble.hp <= 0:
                Objects.food.append(Food.spawn_food(bubble.x, bubble.y))
                del Objects.bubbles[Objects.bubbles.index(bubble)]

            if C.border + bubble.radius <= bubble.x + bubble.current_vec[0] <= C.width - C.border - bubble.radius:
                bubble.x += bubble.current_vec[0]
            else:
                bubble.current_vec = (bubble.current_vec[0] * -1, bubble.current_vec[1])
            if C.border + bubble.radius <= bubble.y + bubble.current_vec[1] <= int(C.st_proportion * C.height) - \
                    C.border - bubble.radius:
                bubble.y += bubble.current_vec[1]
            else:
                bubble.current_vec = (bubble.current_vec[0], bubble.current_vec[1] * -1)

            if Objects.n == C.frm_rate:
                bubble.current_vec = Bbl.move(bubble.speed)

        if Objects.n == C.frm_rate:
            Objects.n = 0

    @staticmethod
    def update_food(chance, max_quantity):
        if len(Objects.food) < max_quantity:
            if randint(0, 100) < chance:
                Objects.food.append(Food(food=False))
            else:
                Objects.food.append(Food())

    @staticmethod
    def render_bubbles(game_display):
        for bubble in Objects.bubbles:
            pygame.draw.circle(game_display, bubble.color, (bubble.x, bubble.y), bubble.radius)

    @staticmethod
    def render_food(game_display):
        for food in Objects.food:
            pygame.draw.rect(game_display, food.color, (food.x, food.y, food.width, food.height))

