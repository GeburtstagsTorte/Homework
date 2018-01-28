import pygame
from Constants import GameConstants as GC


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


def main():
    pygame.init()

    Game(GC.game_name, GC.width, GC.height, GC.background_color, game_icon=GC.images["game_icon"])

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
