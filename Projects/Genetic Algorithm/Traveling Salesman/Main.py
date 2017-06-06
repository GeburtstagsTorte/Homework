"""
TO DO:

    [x] Brute Force bug fix
    [] Match results
    [x] center cities

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
    clock = pygame.time.Clock()
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
            self.clock.tick(60)

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

        self.update_buttons()

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

        txt_fitness_bf = font2.render("fitness: {}".format(BruteForce.best[1]), True, C.text_color)
        txt_fitness_ga = font2.render("fitness: {}".format(self.population.best.fitness), True, C.text_color)
        self.game_display.blit(txt_fitness_bf, C.txt_text_bf_pos)
        self.game_display.blit(txt_fitness_ga, C.txt_text_ga_pos)

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

    def update_buttons(self):
        if self.restart_button.clicked(self.mouse_click):
            self.cities = [City(self.game_display, self.width, self.height, C.city_color, C.city_radius)
                           for i in range(C.city_amount)]
            self.scale_cities()
            self.population = Population(C.max_population, C.mutation_rate, self.cities)
            BruteForce.best = ([], 0)
            self.bf_route = BruteForce.initialize_route(C.city_amount)
            self.count = 1

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
