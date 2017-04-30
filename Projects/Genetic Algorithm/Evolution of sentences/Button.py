import pygame


class Button:

    visible = True
    locked = False

    def __init__(self, surface, pos, width, height, color=(120, 120, 120), text='', text_size=10, text_color=(0, 0, 0),
                 font='Arial', image=None, image2=None, mod=None, border=None, extend=False):

        self.surface = surface
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color                      # rgb
        self.text = text                        # default blank
        self.font = font                        # default Arial
        self.text_color = text_color            # default black // (0, 0, 0)
        self.image = image                      # default None , default image displayed
        self.image2 = image2                    # default None, image displayed when mouse in button collision box
        self.mod = mod                          # default 1, defines which button appearance
        self.border = border                    # default None, draws line
        self.extend = extend                    # default False, extends button if mouse is in button area

        # example: border = (255, 255, 255) rgb
        #   > white border

        # mod 1:
        #   basic rect

        # mod 2:
        #   rect and semi-circles
        self.text_size = shift_size(text, text_size, font, width)

        if image is not None:
            self.image = pygame.image.load(self.image)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def render(self):
        pos = self.pos
        color = self.color
        image = self.image
        width, height = self.width, self.height

        if self.visible:

            # change button if mouse is in collision box

            if self.collide():
                if self.image2 is not None:
                    image = pygame.image.load(self.image2)
                    image = pygame.transform.scale(image, (self.width, self.height))

                else:
                    color = (25, 25, 25) if self.color == (0, 0, 0) else self.color
                    color = tuple(int(color[i] * 0.8) for i in range(len(color)))

                if self.extend:
                    if self.image is not None and self.image2 is None:
                        image = pygame.transform.scale(self.image, (int(self.width * 1.1), int(self.height * 1.1)))

                    elif self.image2 is not None:
                        image = pygame.transform.scale(self.image2, (int(self.width * 1.1), int(self.height * 1.1)))

                    pos = [self.pos[0] - int(self.width * 0.025), self.pos[1] - int(self.height * 0.025)]
                    width = int(self.width * 1.05)
                    height = int(self.height * 1.05)

            # drawing buttons based on mod

            if self.mod is None:
                if self.border is not None:
                    pygame.draw.rect(self.surface, self.border,
                                     (pos[0] - 1, pos[1] - 1, width + 2, height + 2))
                self.surface.blit(image, pos)

            elif self.mod == 1:
                if self.border is not None:
                    pygame.draw.rect(self.surface, self.border,
                                     (pos[0] - 1, pos[1] - 1, width + 2, height + 2))

                pygame.draw.rect(self.surface, color, (pos[0], pos[1], width, height))

            elif self.mod == 2:
                if self.border is not None:
                    pygame.draw.rect(self.surface, self.border,
                                     (pos[0], pos[1] - 1, width + 1, height + 2))
                    pygame.draw.circle(self.surface, self.border, [pos[0], pos[1] + height // 2], height//2 + 1)
                    pygame.draw.circle(self.surface, self.border, [pos[0]+width, pos[1]+height//2], height//2 + 1)

                pygame.draw.circle(self.surface, color, [pos[0], pos[1] + height // 2], height // 2)
                pygame.draw.circle(self.surface, color, [pos[0] + width, pos[1] + height // 2], height // 2)
                pygame.draw.rect(self.surface, color, (pos[0], pos[1], width, height))

            # drawing text

            font = pygame.font.SysFont(self.font, self.text_size)
            txt = font.render(self.text, True, self.text_color)
            txt_rect = txt.get_rect(center=(pos[0] + 0.5 * width, pos[1] + 0.5 * height))

            self.surface.blit(txt, txt_rect)

    def update(self):
        pass

    def clicked(self, mouse_click):
        if self.collide() and mouse_click and self.visible and not self.locked:
            return True
        return False

    def collide(self):
        x, y = pygame.mouse.get_pos()

        if self.mod == 1 or self.mod is None:

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
        return shift_size(text, size - dec_by, font, max_length, dec_by)
    return size
