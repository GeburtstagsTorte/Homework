import pygame
from Constants import C
from Population_class_version import Population
from Button import Button


class Game:
    clock = pygame.time.Clock()
    game_exit = False
    pop = object

    def __init__(self, title, width, height, background_color=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)

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
            self.clock.tick(60)

    def render(self):
        self.draw_structure()
        self.draw_info()
        self.button()

    def update(self):
        # Entities.update()
        if self.pop.best.fitness < 1:
            self.pop.update()

    def draw_info(self):

        # draw current best individual
        best_string = ""
        for i in self.pop.best.genes:
            best_string += i

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
            self.game_display.blit(label_list[line], (pos[0],  pos[1] + 10*line + line*C.info_size + 20))

    def draw_current_population(self):
        start_pos = (3*self.width//4 + 20, 20)
        for individual in self.pop.population:
            string = ""
            for i in individual.genes:
                string += i

    def draw_structure(self):
        pygame.draw.line(self.game_display, C.structure_color, (3*self.width//4, 0), (3*self.width//4, self.height))
        pygame.draw.line(self.game_display, C.structure_color, (0, self.height//2), (3*self.width//4, self.height//2))
        # draw graph structure

    def button(self):
        restart = Button(self.game_display, C.rb_color, 3*self.width//4 - C.rb_length-20, self.height//2-C.rb_height-10,
                         C.rb_length, C.rb_height, C.width, C.height, C.rb_text, C.rb_font, C.rb_text_color, 20)
        restart.draw_button()
        if restart.button_touch():
            self.pop = Population(C.target, C.popmax, C.mutation_rate)

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True


def main():
    pygame.init()

    width = C.width
    height = C.height
    Game("Genetic Algorithm", width, height)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()

