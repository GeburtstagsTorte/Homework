"""
TO DO:

    [x] Brute Force bug fix
    [] Match results
    [x] center cities
    [] information
        > GA: last change -> generation, percentage, distance
    [] difference between GA and BF in percentage

"""

import pygame
import decimal
from Constants import C
from Cities import City
from Population import Population
from Route import Route
from Brute_Force import BruteForce
from math import factorial
from Button import Button
from textbox import CenterBox


class Game:

    game_exit = False
    mouse_click = False
    cities = []
    record = Route([], 0)
    restart_button = object

    def __init__(self, title, width, height, background_color=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)

        self.cities = [City(self.game_display, self.width, self.height, C.city_color, C.city_radius)
                       for i in range(C.city_amount)]
        self.scale_cities()
        self.population = Population(C.max_population, C.mutation_rate, self.cities)
        self.bf_route = BruteForce.initialize_route(C.city_amount)
        BruteForce.calculate_best(self.bf_route, self.cities)
        self.count = 1

        self.initialize_buttons()
        self.main_loop()

    def main_loop(self):
        while not self.game_exit:

            for event in pygame.event.get():
                self.handle_keys(event)

            self.game_display.fill(self.background_color)
            self.render()
            pygame.display.update()
            self.update()
            self.mouse_click = False

    def render(self):
        self.structure()
        self.restart_button.render()

        # Route.draw_best_route(self.game_display, self.population.best, self.cities, width=C.route_width)
        BruteForce.draw_route(self.game_display, self.cities, self.bf_route)
        BruteForce.draw_route(self.game_display, self.cities, BruteForce.best[0], color=C.bf_color)

        City.render_cities(self.cities)
        Route.draw_ga_only(self.game_display, C.GA_path_color, self.population.best.genes, self.cities)
        self.handle_text()

    def update(self):

        if self.population.best.fitness > self.record.fitness:
            self.record = self.population.best
        self.population.update()

        BruteForce.calculate_best(self.bf_route, self.cities)
        if self.count < factorial(C.city_amount):
            self.bf_route = BruteForce.permute(self.bf_route, self.cities)
            self.count += 1
            self.population.count += 1

        self.update_buttons()

    def update_buttons(self):
        if self.restart_button.clicked(self.mouse_click):
            self.cities = [City(self.game_display, self.width, self.height, C.city_color, C.city_radius)
                           for i in range(C.city_amount)]
            self.scale_cities()
            self.population = Population(C.max_population, C.mutation_rate, self.cities)
            BruteForce.best = ([], 0)
            self.bf_route = BruteForce.initialize_route(C.city_amount)
            self.count = 1

    def structure(self):
        pygame.draw.line(self.game_display, C.structure_color, (0.75*self.width, 0), (0.75*self.width, self.height),
                         C.st_width)
        pygame.draw.line(self.game_display, C.structure_color, (0, 0.5*self.height + C.border),
                         (0.75*self.width, 0.5*self.height + C.border), C.st_width)

    def handle_text(self):
        font = pygame.font.SysFont(C.font, C.head_size)

        txt_head = font.render("{} {}%".format(C.txt_head1, round(decimal.Decimal(self.count/factorial(C.city_amount)
                                                                                  * 100), 2)), True, C.text_color)
        txt_head2 = font.render("{}".format(C.txt_head2), True, C.text_color)
        self.game_display.blit(txt_head, C.txt_head1_pos)
        self.game_display.blit(txt_head2, C.txt_head2_pos)

        font2 = pygame.font.SysFont(C.font, C.size)

        # txt_fitness_bf = font2.render("fitness: {}".format(BruteForce.best[1]), True, C.text_color)
        # txt_fitness_ga = font2.render("fitness: {}".format(self.population.best.fitness), True, C.text_color)
        # self.game_display.blit(txt_fitness_bf, C.txt_text_bf_pos)
        # self.game_display.blit(txt_fitness_ga, C.txt_text_ga_pos)

        bf_label_list = []
        ga_label_list = []

        if BruteForce.best[1] > 0 and self.population.best.fitness > 0:
            bf_information_list = [
                "fitness      : {}".format(round(decimal.Decimal(BruteForce.best[1]), 7)),
                "distance     : {}".format(round(decimal.Decimal(1 / BruteForce.best[1]), 7)),
                "discrepancy  : {}%".format((round(decimal.Decimal((self.population.best.fitness - BruteForce.best[1]) /
                                                   self.population.best.fitness * 100), 3)))
            ]

            ga_information_list = [
                "fitness      : {}".format(round(decimal.Decimal(self.population.best.fitness), 7)),
                "distance     : {}".format(round(decimal.Decimal(1 / self.population.best.fitness), 7)),
                "mutation rate: {}".format(C.mutation_rate),
                "population   : {}".format(C.max_population),
                "last change:",
                "generation   : {}".format(self.population.last_gen),
                "percentage   : {}%".format(round(decimal.Decimal(self.population.last_count/factorial(C.city_amount)
                                                                  * 100), 2))
            ]

            for line in bf_information_list:
                bf_label_list.append(font2.render(line, True, C.text_color))

            for line in ga_information_list:
                ga_label_list.append(font2.render(line, True, C.text_color))

            for line in range(len(bf_label_list)):
                self.game_display.blit(bf_label_list[line], (C.txt_text_bf_pos[0], C.txt_text_bf_pos[1] + 10*line +
                                                             line*C.size))

            for line in range(len(ga_label_list)):
                self.game_display.blit(ga_label_list[line], (C.txt_text_ga_pos[0], C.txt_text_ga_pos[1] + 10*line +
                                                             line*C.size))

    def scale_cities(self):
        pos_list = [i.pos for i in self.cities]
        max_width, max_height = CenterBox.identify_max_length(pos_list)
        start_pos = CenterBox.identify_pos(pos_list)

        d_pos = CenterBox.scale_pos(start_pos, C.frame1_pos, max_width, max_height, C.frame1_width, C.frame1_height, 1)

        for city in self.cities:
            city.pos = (city.pos[0] + d_pos[0], city.pos[1] + d_pos[1])
            city.x = city.pos[0] + d_pos[0]
            city.y = city.pos[1] + d_pos[1]

    def initialize_buttons(self):
        self.restart_button = Button(self.game_display, C.btn_pos, C.btn_width, C.btn_height, C.btn_color, C.rb_text,
                                     C.btn_txt_size, C.btn_text_color, mod=2, border=C.btn_border_color)

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.mouse_click = True


def main():
    pygame.init()

    width = C.width
    height = C.height
    background_color = C.background_color
    Game("Genetic Algorithm - Traveling Salesman", width, height, background_color)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
