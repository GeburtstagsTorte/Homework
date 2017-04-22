# Simon
import pygame
import math
from pygame.locals import *


class Game:
    clock = pygame.time.Clock()
    game_exit = False

    def __init__(self, title, width, height, background_color=(200, 200, 200)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)
        self.main_loop()

    def main_loop(self):
        while not self.game_exit:

            self.game_display.fill(self.background_color)
            FractalBranch.generate_branches(self.game_display, 5, 45, 250, (500, 1000), (500, 1000-250))
            pygame.display.update()
            self.clock.tick(60)

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True


class FractalBranch:
    black = (0, 0, 0)

    def __init__(self, branch_length, start_coords, end_coords):
        self.branch_length = branch_length
        self.start_coords = start_coords
        self.end_coords = end_coords

    @staticmethod
    def generate_branches(game_display, tree_length, angle, branch_length, start_coords, end_coords):
        temporary_branches = []
        branches = []
        branches.append(FractalBranch(branch_length, start_coords, end_coords))
        for i in range(tree_length):
            for j in range(len(temporary_branches)):
                x = temporary_branches[j].end_coords[0] + math.cos(angle) * branch_length // len(temporary_branches)
                y = temporary_branches[j].end_coords[1] + math.cos(angle) * branch_length // len(temporary_branches)
                branches.append(
                    FractalBranch(branch_length // len(temporary_branches), temporary_branches[j].end_coords,
                                  (x, y)))
                branches.append(
                    FractalBranch(branch_length // len(temporary_branches), temporary_branches[j].end_coords,
                                  (1000 - x, y)))
                temporary_branches = branches[len(temporary_branches)*2:]
        for k in range(len(branches)):
            pygame.draw.line(game_display, FractalBranch.black, branches[k].start_coords, branches[k].end_coords)


def main():
    pygame.init()
    Game("fractals", 1000, 1000)
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
