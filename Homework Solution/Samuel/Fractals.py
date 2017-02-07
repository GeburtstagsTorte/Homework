import pygame
import math


class Main:
    game_exit = False
    size = width, height = 800, 600
    background_color = (32, 32, 32)

    def __init__(self, radius, delta_angle):
        pygame.init()
        self.radius = radius
        self.delta_angle = delta_angle
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Fractals")
        self.main_loop()

    def main_loop(self):
        while not self.game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exit = True

            self.screen.fill(self.background_color)
            Fractal((self.width//2, self.height - 100), -90, self.screen, self.radius, self.delta_angle)
            pygame.display.update()

        quit()
        pygame.quit()


class Fractal:

    color = (255, 255, 255)

    def __init__(self, start_pos, angle, surface, radius, delta_angle):
        self.start_pos = self.x, self.y = start_pos
        self.angle = angle
        self.surface = surface
        self.radius = radius
        self.delta_angle = delta_angle
        self.loop()

    def loop(self):
        end_pos = self.radius * math.cos(math.radians(self.angle)) + self.x,\
                  self.radius * math.sin(math.radians(self.angle)) + self.y
        pygame.draw.line(self.surface, self.color, self.start_pos, end_pos, 2)
        if self.radius > 1:
            Fractal(end_pos, self.angle + self.delta_angle, self.surface, 2*self.radius//3, self.delta_angle)
            Fractal(end_pos, self.angle - self.delta_angle, self.surface, 2*self.radius//3, self.delta_angle)


if __name__ == '__main__':
    Main(150, 30)
