import pygame
from Constants import GameConstants as GC
from Textboxes import Text
from Objects import Objects
from math import factorial
from decimal import Decimal


class Game:
    clock = pygame.time.Clock()
    game_exit = False
    mouse_click = False

    def __init__(self, title, width, height, background_color, game_icon):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)

        if game_icon is not None:
            pygame.display.set_icon(game_icon)

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.mouse_click = True


class Frame(Game):

    def __init__(self, title, width, height, background_color, game_icon):
        super().__init__(title, width, height, background_color, game_icon)
        self.Obj = Objects()
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
            # self.clock.tick(GC.tick)

    def render(self):
        self.draw_structure()
        self.draw_text()
        GC.btn_restart.render(self.game_display)

        for city in self.Obj.cities:
            city.render(self.game_display)

        self.Obj.render(self.game_display)

    def update(self):
        if GC.btn_restart.clicked(self.mouse_click):
            main()
        self.Obj.update()

    def draw_structure(self):
        pygame.draw.line(self.game_display, GC.colors["white"], (0.75 * self.width, 0),
                         (0.75 * self.width, self.height))
        pygame.draw.line(self.game_display, GC.colors["white"], (0, 0.5 * self.height),
                         (self.width, 0.5 * self.height))

    def draw_text(self):
        font = pygame.font.SysFont(GC.font, GC.txt_size + 5)

        txt_head2 = font.render("{} {}%".format(GC.txt_head2, round(Decimal((self.Obj.count / factorial(GC.city_total))
                                                                            * 100), 2)), True, GC.txt_color)
        txt_head1 = font.render("{}".format(GC.txt_head1),
                                True, GC.txt_color)

        ga_information_list = [
            "distance     : {}".format(round(self.Obj.ga_best.distance, 3)),
            "last change  : {}".format(self.Obj.last_gen),
            "population   : {}".format(GC.population_size),
            "mutation rate: {}%".format(GC.mutation_rate)
        ]

        bf_information_list = [
            "distance     : {}".format(round(Decimal(self.Obj.bf_best.distance), 3)),
            "tries        : {}".format(self.Obj.last_count),
            "discrepancy  : {}%".format(round(abs(Decimal((1 - self.Obj.ga_best.distance + self.Obj.bf_best.distance)
                                                          * 100 / self.Obj.ga_best.distance)), 3))
        ]

        ga_label_list = Text.render_text(GC.font, GC.txt_size, GC.txt_color, ga_information_list)
        bf_label_list = Text.render_text(GC.font, GC.txt_size, GC.txt_color, bf_information_list)

        self.game_display.blit(txt_head1, GC.txt_head1_pos)
        self.game_display.blit(txt_head2, GC.txt_head2_pos)

        for line in range(len(ga_label_list)):
            self.game_display.blit(ga_label_list[line], (GC.txt_head1_pos[0], GC.txt_head1_pos[1] + 10 * (line + 1) +
                                                         (line + 1) * GC.txt_size))

        for line in range(len(bf_label_list)):
            self.game_display.blit(bf_label_list[line], (GC.txt_head2_pos[0], GC.txt_head2_pos[1] + 10 * (line + 1) +
                                                         (line + 1) * GC.txt_size))


def main():
    GC()
    Frame(GC.game_name, GC.width, GC.height, GC.background_color, game_icon=GC.images["game_icon"])

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
