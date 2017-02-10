import pygame
import math
# No Constants therefore it is pretty messy


class Main:
    game_exit = False
    size = width, height = 800, 600
    background_color = (32, 32, 32)
    mouse_down = False

    delta_angle = 30
    # Regulator
    reg_x, circle_x = 50, 50
    reg_y = height - 50
    reg_length = 80
    reg_radius = 5

    def __init__(self, radius):
        pygame.init()
        pygame.display.set_caption("Fractals")
        self.radius = radius
        self.screen = pygame.display.set_mode(self.size)
        self.main_loop()

    def main_loop(self):

        while not self.game_exit:
            self.handle_keys()
            self.screen.fill(self.background_color)
            Regulator((self.reg_x, self.reg_y), (self.reg_x + self.reg_length, self.reg_y),
                      self.screen, self.mouse_down, self.reg_radius, self.circle_x)
            Fractal((self.width//2, self.height - 100), -90, self.screen, self.radius, self.delta_angle)
            pygame.display.update()

        quit()
        pygame.quit()

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False


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


class Regulator:

    color = (255, 255, 255)

    def __init__(self, start_pos, end_pos, surface, mouse_down, radius, circle_x):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.surface = surface
        self.mouse_down = mouse_down
        self.radius = radius
        self.circle_x = circle_x
        self.update()
        self.draw()

    def draw(self):
        pygame.draw.line(self.surface, self.color, self.start_pos, self.end_pos)
        pygame.draw.circle(self.surface, self.color, (self.circle_x, self.start_pos[1]), self.radius)

    def touched(self, x, y):
        if self.start_pos[0] <= x <= self.end_pos[0] and self.mouse_down and \
                (self.radius + 10)**2 >= (self.circle_x - x)**2 + (self.start_pos[1] - y)**2:
            return True
        return False

    def update(self):
        x, y = pygame.mouse.get_pos()
        phi = 330 // (self.end_pos[0]- self.start_pos[0])
        prev_x = Main.circle_x
        if self.touched(x, y):

            if x > Main.circle_x:
                Main.delta_angle += (prev_x - x)*phi
            else:
                Main.delta_angle += (prev_x - x)*phi
            Main.circle_x = x

if __name__ == '__main__':
    Main(150)
