import pygame
from Constants import Constants as C
from Objects import Objects as Obj


class Game:
    clock = pygame.time.Clock()
    game_exit = False
    game_pause = False
    mouse_click = False

    def __init__(self, title, width, height, background_color=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)

        Obj.init_objects(self.game_display)
        self.main_loop()

    def main_loop(self):
        while not self.game_exit:

            for event in pygame.event.get():
                self.handle_keys(event)

            self.game_display.fill(self.background_color)
            self.render(self.game_display)
            pygame.display.update()
            self.update()
            self.mouse_click = False
            self.clock.tick(60)

    @staticmethod
    def render(game_display):
        Obj.structure(game_display, C.width, C.height, C.st_color, C.st_proportion)
        Obj.btn_pause.render()
        Obj.btn_restart.render()
        Obj.render_bubbles(game_display)
        Obj.render_food(game_display)

    def update(self):
        if Obj.btn_pause.clicked(self.mouse_click):
            self.game_pause = not self.game_pause

            if self.game_pause:
                Obj.btn_pause.text = C.ps_text2
            else:
                Obj.btn_pause.text = C.ps_text

        if Obj.btn_restart.clicked(self.mouse_click):
            Obj.time = 0
            Obj.n = 0
            Obj.bbl1, Obj.bbl2, Obj.bbl3, Obj.bubbles, Obj.food = [], [], [], [], []
            Obj.init_bubbles(C.quantity, C.q_bubble)

        if not self.game_pause:
            if Obj.time == C.year:
                Obj.time = 0
            else:
                Obj.time += 1
            Obj.update_food(C.chance, C.fd_max_quantity)
            Obj.update_bubbles()

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.mouse_click = True


def main():
    pygame.init()

    width = C.width
    height = C.height
    name = C.name

    Game(name, width, height, C.background_color)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
