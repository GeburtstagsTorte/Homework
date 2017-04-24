import pygame


class Button:

    visible = True

    def __init__(self, surface, pos, width, height, color, text='', text_size=10, text_color=(0, 0, 0),
                 font='Arial', image=None, mod=1, border=None):
        self.surface = surface
        self.pos = pos                  # tuple or list
        self.width = width
        self.height = height
        self.color = color              # rgb
        self.text = text                # default blank
        self.font = font                # default Arial
        self.text_color = text_color    # default black // (0, 0, 0)
        self.image = image              # default None
        self.mod = mod                  # default 1
        self.border = border            # default None
        # example: border = (255, 255, 255) rgb
        #   > white border

        # mod 1:
        #   basic rect

        # mod 2:
        #   rect and semi-circles
        self.text_size = shift_size(text, text_size, font, width)

        if image is not None:
            self.mod = None

    def render(self):
        if self.visible:
            if self.collide():
                color = (25, 25, 25) if self.color == (0, 0, 0) else self.color
                color = tuple(int(color[i] * 0.8) for i in range(len(color)))
            else:
                color = self.color

            if self.mod is None:
                if self.border is not None:
                    pygame.draw.rect(self.surface, self.border,
                                     (self.pos[0] - 1, self.pos[1] - 1, self.width + 2, self.height + 2))

                image = pygame.image.load(self.image)
                image = pygame.transform.scale(image, (self.width, self.height))

                self.surface.blit(image, self.pos)

            if self.mod == 1:
                if self.border is not None:
                    pygame.draw.rect(self.surface, self.border,
                                     (self.pos[0] - 1, self.pos[1] - 1, self.width + 2, self.height + 2))

                pygame.draw.rect(self.surface, color, (self.pos[0], self.pos[1], self.width, self.height))

            if self.mod == 2:
                if self.border is not None:
                    pygame.draw.rect(self.surface, self.border,
                                     (self.pos[0], self.pos[1] - 1, self.width + 1, self.height + 2))
                    pygame.draw.circle(self.surface, self.border, [self.pos[0], self.pos[1] + self.height // 2],
                                       self.height//2 + 1)
                    pygame.draw.circle(self.surface, self.border, [self.pos[0]+self.width, self.pos[1]+self.height//2],
                                       self.height//2 + 1)

                pygame.draw.circle(self.surface, color, [self.pos[0], self.pos[1] + self.height // 2],
                                   self.height // 2)
                pygame.draw.circle(self.surface, color, [self.pos[0] + self.width, self.pos[1] + self.height // 2],
                                   self.height // 2)
                pygame.draw.rect(self.surface, color, (self.pos[0], self.pos[1], self.width, self.height))

            font = pygame.font.SysFont(self.font, self.text_size)
            txt = font.render(self.text, True, self.text_color)
            txt_rect = txt.get_rect(center=(self.pos[0] + 0.5 * self.width, self.pos[1] + 0.5 * self.height))

            self.surface.blit(txt, txt_rect)

    def update(self):
        pass

    def clicked(self, mouse_click):
        if self.collide() and mouse_click:
            return True
        return False

    def collide(self):
        x, y = pygame.mouse.get_pos()

        if self.mod == 1:

            if self.pos[0] <= x <= self.pos[0] + self.width and self.pos[1] <= y <= self.pos[1] + self.height:
                return True

        elif self.mod == 2:

            if self.pos[0] <= x <= self.pos[0] + self.width and self.pos[1] <= y <= self.pos[1] + self.height \
                    or (self.height // 2)**2 >= (self.pos[0] - x) ** 2 + (self.pos[1] - y + self.height // 2) ** 2 \
                    or (self.height // 2)**2 >= (self.pos[0] + self.width-x)**2 + (self.pos[1]-y + self.height // 2)**2:
                return True
        return False


def shift_size(text, size, font, max_length, dec_by=1):
    fnt = pygame.font.SysFont(font, size)
    txt = fnt.render(text, True, (0, 0, 0))
    txt_length = txt.get_rect()[2]
    if size == 0:
        print("text length is too large")
        return 1
    if txt_length > max_length:
        return Textbox.shift_size(text, size - dec_by, font, max_length, dec_by)
    return size


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300), pygame.SRCALPHA)
    game_exit = False
    mouse_click = False
    button = Button(screen, (50, 50), 120, 40, (0, 0, 0), "Button", 10, (255, 255, 255),
                    border=(255, 255, 255), mod=2)
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            mouse_click = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click = True

        screen.fill((0, 0, 0))
        button.render()
        if button.clicked(mouse_click):
            game_exit = True

        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
