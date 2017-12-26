import pygame
from Constants import GameConstants as GC
from Objects import Objects


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
        pass


def main():
    GC()
    Frame(GC.game_name, GC.width, GC.height, GC.background_color, game_icon=GC.images["game_icon"])

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
