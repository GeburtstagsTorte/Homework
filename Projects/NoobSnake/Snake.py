import pygame
from Constants import Constants as C
from random import randrange


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

    def __init__(self, game_display):
        Objects.add_segment(game_display, C.width // 2, C.height // 2)

    @staticmethod
    def render(game_display):
        Food(Objects.food_x, Objects.food_y, game_display, C.red).render()

        for i in range(len(Objects.segments)):
            Objects.segments[i].render()

        Objects.render_grid(game_display)
        Objects.render_ui(game_display)

        if Objects.game_lost:
            Objects.render_lose_screen(game_display)

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
                Objects.score += 1

    @staticmethod
    def check_if_intersect():
        for i in range(1, len(Objects.segments)):
            if Objects.segments[0].x == Objects.segments[i].x and \
                            Objects.segments[0].y == Objects.segments[i].y:

                Objects.segments[0].color = C.blue
                Objects.segments[i].color = C.blue
                return True
        return False
