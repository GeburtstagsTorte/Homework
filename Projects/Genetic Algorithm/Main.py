"""
TO DO:
    [>]create buttons: Restart, Pause
    >create log:
        txt file with results
    >drawing results/log
"""

import pygame
from Constants import C
from Population_class_version import Population
from textbox import Textbox
from Button import Button
from Log import update_log, get_log


class Game:
    clock = pygame.time.Clock()
    game_exit = False
    mouse_click = False
    game_pause = False
    pop = object
    restart_button = object
    pause_button = object
    log_enabled = True

    def __init__(self, title, width, height, background_color=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)
        self.initialize_buttons()

        self.pop = Population(C.target, C.popmax, C.mutation_rate)

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
        self.draw_structure()
        self.draw_info()
        self.draw_current_population()
        self.draw_log()

        self.restart_button.render()
        self.pause_button.render()

    def update(self):
        self.buttons_update()

        if not self.game_pause:
            if self.pop.best.fitness < 1:
                self.pop.update()
            if self.pop.best.fitness == 1:
                self.write_log()
                self.log_enabled = False

    def draw_info(self):

        # draw current best individual
        """best_string = ""
        for i in self.pop.best.genes:
            best_string += i"""
        best_string = ''.join(self.pop.best.genes)

        font = pygame.font.SysFont(C.font, C.best_size)
        txt = font.render(best_string, True, C.text_color)
        self.game_display.blit(txt, C.best_pos)

        # draw general information
        pos = (C.best_pos[0], C.best_pos[1] + txt.get_rect()[3])
        info_font = pygame.font.SysFont(C.font, C.info_size)
        label_list = []

        information_list = ["generation     : {}".format(self.pop.generation),
                            "average fitness: {}%".format(round(self.pop.average_fitness*100, 3)),
                            "best fitness   : {}%".format(round(self.pop.best.fitness*100, 3)),
                            "population     : {}".format(C.popmax),
                            "mutation rate  : {}%".format(C.mutation_rate)]

        for line in information_list:
            label_list.append(info_font.render(line, True, C.text_color))

        for line in range(len(label_list)):
            self.game_display.blit(label_list[line], (pos[0],  pos[1] + 10*line + line*C.info_size + 50))

    def draw_current_population(self):
        # center text:
        # (x, y, width_X, length_Y) (textbox)

        row_pitch = C.row_pitch
        max_length = self.width//4 - 2*row_pitch
        center_pos = [7*self.width//8, 0]
        sample = ''.join(self.pop.population[0].genes)

        size = Textbox.shift_size(sample, C.pop_size, C.font, max_length)
        font = pygame.font.SysFont(C.font, size)
        n = 0

        for individual in self.pop.population:
            string = ''.join(individual.genes)

            txt = font.render(string, True, C.text_color)

            center_pos[1] += + size * (n + 1) + row_pitch
            txt_rect = txt.get_rect(center=center_pos)

            if center_pos[1] < self.height - row_pitch - txt.get_rect()[3]:
                self.game_display.blit(txt, txt_rect)

    def draw_structure(self):
        pygame.draw.line(self.game_display, C.structure_color, (3*self.width//4, 0), (3*self.width//4, self.height))
        pygame.draw.line(self.game_display, C.structure_color, (0, self.height//2), (3*self.width//4, self.height//2))
        # draw graph structure

    def buttons_update(self):

        if self.restart_button.clicked(self.mouse_click):
            self.pop = Population(C.target, C.popmax, C.mutation_rate)
            self.log_enabled = True

        if self.pause_button.clicked(self.mouse_click):
            self.game_pause = not self.game_pause
            # self.restart_button.locked = True

            if self.game_pause:
                self.pause_button.text = "Resume"
            else:
                self.pause_button.text = C.ps_text

    def initialize_buttons(self):
        self.restart_button = Button(self.game_display,
                                     (self.width // 2 + C.rb_length, self.height // 2 - C.rb_height - 10), C.rb_length,
                                     C.rb_height, C.rb_color, C.rb_text, C.rb_text_size, C.rb_text_color, C.rb_font,
                                     mod=2, border=C.rb_border, extend=True)
        self.pause_button = Button(self.game_display,
                                   (self.width // 2 + C.ps_length,
                                    self.height // 2 - C.ps_height - 10 - C.ps_height - 10),
                                   C.ps_length, C.ps_height, C.ps_color, C.ps_text, C.ps_text_size, C.ps_text_color,
                                   C.ps_font, mod=2, border=C.ps_border, extend=True)

    def write_log(self):
        if self.log_enabled:
            string = ''.join(self.pop.best.genes)
            info = [string,
                    str(self.pop.generation),
                    str(self.pop.average_fitness),
                    str(self.pop.popmax),
                    str(self.pop.mutation_rate)
                    ]

            update_log(info)

    def draw_log(self):
        info = get_log()
        info = info[len(info)-1]
        # for info in log:
        if info is not None:
            information_list = [
                'sentence       : {}'.format(info[0]),
                'generation     : {}'.format(info[1]),
                'average fitness: {}%'.format(round(float(info[2])*100, 3)),
                'population     : {}'.format(info[3]),
                'mutation rate  : {}%'.format(info[4])
            ]

            label_list = []
            info_font = pygame.font.SysFont(C.font, C.log_size)

            pos = (C.best_pos[0], 0.5 * self.height + C.row_pitch)

            txt = pygame.font.SysFont(C.font, C.log_size + 5).render("Last Evolution: ", True, C.text_color)
            self.game_display.blit(txt, pos)

            for line in information_list:
                label_list.append(info_font.render(line, True, C.text_color))

            for line in range(len(label_list)):
                self.game_display.blit(label_list[line], (pos[0],  pos[1] + (line + 1)*C.info_size))

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.mouse_click = True


def main():
    pygame.init()

    width = C.width
    height = C.height
    Game(C.game_name, width, height, C.background_color)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()

