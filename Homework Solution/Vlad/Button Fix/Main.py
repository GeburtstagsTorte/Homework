import pygame
from Button import Button


class App:
    clock = pygame.time.Clock()
    game_exit = False

    def __init__(self, title, width, height, background_color=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)

        self.button = Button(self.game_display, 0, 0, 100, 100, (255, 0, 0), "Hello World", "Arial", 10, (0, 0, 0))

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

    def render(self, game_display):
        self.button.draw_button()

    def update(self):
        pass

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True

if __name__ == "__main__":
    pygame.init()
    App("", 500, 500)
    pygame.quit()
    exit()