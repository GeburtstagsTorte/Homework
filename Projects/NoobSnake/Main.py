from Constants import Constants as C
from Snake import Objects as Obj
import pygame


class Game:
    clock = pygame.time.Clock()
    game_exit = False
    game_start = False
    mouse_click = False

    def __init__(self, title, width, height, background_color=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        Obj(self.game_display)
        pygame.display.set_caption(title)
        pygame.display.set_icon(C.game_icon)
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
            self.clock.tick(15)

    def render(self):
        if self.game_start:
            Obj.render_game(self.game_display, self.mouse_click)
        else:
            Obj.render_menu(self.game_display, self.mouse_click)
            if Obj.handle_start_button(self.mouse_click):
                self.game_start = True
            if Obj.handle_exit_button(self.mouse_click):
                self.game_exit = True

    def update(self):
        if self.game_start:
            Obj.update(self.game_display)

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.mouse_click = True

        Obj.handle_keys(event)


def main():
    pygame.init()

    width = C.width
    height = C.height
    name = C.game_name
    background_color = C.background_color
    Game(name, width, height, background_color)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
