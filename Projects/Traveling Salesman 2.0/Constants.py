from Button import Button
import pygame


class GameConstants:

    def __init__(self):
        pygame.init()

    width = 1200
    height = 800

    game_name = "Traveling Salesman 2.0"
    tick = 60

    images = {
        "game_icon": None,
    }

    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "dark_red": (139, 0, 0),
        "crimson": (220, 20, 60),
        "green": (0, 128, 0),
        "lime": (0, 255, 0),
        "forest_green": (34, 139, 34),
        "blue": (0, 0, 255),
        "navy": (0, 0, 128),
        "turquoise": (64, 224, 208),
        "0080FF": (0, 128, 255),
        "yellow": (255, 255, 0),
        "orange": (255, 165, 0),
        "dark_orange": (204, 141, 53),
        "gold": (255, 215, 0),
        "grey": (64, 64, 64),
        "dark_grey": (30, 30, 30),
        "light_grey": (128, 128, 128),
        "silver": (192, 192, 192)
    }

    background_color = colors["dark_grey"]
    border = 5

    # Text
    font = 'Courier New'
    txt_color = colors["white"]
    txt_size = 15

    txt_head1 = "Genetic Algorithm"
    txt_head2 = "Brute Force"
    txt_head1_pos = (int(0.75 * width) + border, border)
    txt_head2_pos = (int(0.75 * width) + border, border + int(0.5 * height))

    # Genetic Algorithm
    city_radius = 6
    city_total = 12

    population_size = 100
    mutation_rate = 75

    frame1_pos = (0, 0)
    frame1_width = int(0.75*width)
    frame1_height = int(0.5*height)

    frame2_pos = (0, int(0.5*height))
    frame2_width = int(0.75*width)
    frame2_height = int(0.5*height)

    # Buttons
    btn_width = 120
    btn_height = 40

    btn_restart = Button((width - btn_width - 2*border - btn_height // 2, height - btn_height - 2*border), btn_width,
                         btn_height, background_color, 'new!', text_color=colors["orange"], font=font, mod=2,
                         border=colors["orange"], extend=True)
