import pygame


class Game:
    clock = pygame.time.Clock()
    game_exit = False

    def __init__(self, title, width, height, background_color=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)
        self.main_loop()

    def main_loop(self):
        while not self.game_exit:

            for event in pygame.event.get():
                self.handle_keys(event)

            self.game_display.fill(self.background_color)
            self.render(self.game_display)
            pygame.display.update()
            self.update()
            self.clock.tick(60)

    @staticmethod
    def render(game_display):
        pass

    @staticmethod
    def update():
        # Entities.update()
        pass

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True

    @staticmethod
    def render_graph(surface, color, start_pos, mid_pos, end_pos):
        pass


def main():
    pygame.init()

    width = C.width
    height = C.height
    Game("Genetic Algorithm", width, height)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
