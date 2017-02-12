import pygame
from Constants import C
from Entities import Entities

# TO DO: Adding transparency for particles
#        Correcting curves


class Main:
    clock = pygame.time.Clock()
    game_exit = False

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Gravity")
        self.screen = pygame.display.set_mode(C.size)
        # s = pygame.Surface(C.size)

        self.entities = Entities(self.screen)
        self.main_loop()

    def main_loop(self):
        self.screen.fill(C.background_color)

        while not self.game_exit:
            self.handle_keys()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

        quit()
        pygame.quit()

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_exit = True

    def draw(self):
        self.entities.update()

if __name__ == '__main__':
    Main()
