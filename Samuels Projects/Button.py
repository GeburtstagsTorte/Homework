import pygame


class Button:

    def __init__(self, surface, color, x_coord, y_coord, x_length, y_length, width, height, text, font, text_color, s):
        self.width, self.height = width, height
        self.x_coord, self.y_coord = x_coord, y_coord
        self.x_length, self.y_length = x_length, y_length
        self.color, self.text = color, text
        self.font, self.text_color = font, text_color
        self.surface, self.s = surface, s

    def draw_button(self):
        if self.button_touch():
            self.color = tuple(int(self.color[i]*0.8) for i in range(len(self.color)))

        pygame.draw.circle(self.surface, self.color, [self.x_coord, self.y_coord+(self.y_length//2)], self.y_length//2)
        pygame.draw.circle(self.surface, self.color, [self.x_coord+self.x_length, self.y_coord+(self.y_length//2)],
                           self.y_length // 2)
        pygame.draw.rect(self.surface, self.color, (self.x_coord, self.y_coord, self.x_length, self.y_length))

        font = pygame.font.SysFont(self.font, self.s)
        txt = font.render(self.text, True, self.text_color)
        txt_rect = txt.get_rect(center=(self.x_coord + 0.5*self.x_length, self.y_coord + 0.5*self.y_length))

        while (txt_rect.width > self.x_length or txt_rect.height > self.y_length) and self.s > 0:
            self.s -= 1
            txt = pygame.font.SysFont(self.font, self.s).render(self.text, True, self.text_color)
            txt_rect = txt.get_rect(center=(self.x_coord + 0.5 * self.x_length, self.y_coord + 0.5 * self.y_length))
        self.surface.blit(txt, txt_rect)

    def button_touch(self):
        x, y = pygame.mouse.get_pos()
        if self.x_coord <= x <= self.x_coord + self.x_length and self.y_coord <= y <= self.y_coord + self.y_length or \
            (self.y_length // 2)**2 >= (self.x_coord - x) ** 2 + (self.y_coord - y + self.y_length // 2) ** 2 or \
            (self.y_length // 2)**2 >= (self.x_coord + self.x_length - x)**2 + (self.y_coord - y + self.y_length//2)**2:
            return True
