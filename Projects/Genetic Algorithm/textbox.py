import ctypes
import pygame
from Button import Button


def gtd(text, points, font):
    # thanks a lot anon :*
    # get_text_dimensions
    class SIZE(ctypes.Structure):
        _fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]

    hdc = ctypes.windll.user32.GetDC(0)
    hfont = ctypes.windll.gdi32.CreateFontA(-points, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font)
    hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)
    size = SIZE(0, 0)
    ctypes.windll.gdi32.GetTextExtentPoint32A(hdc, text, len(text), ctypes.byref(size))
    ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
    ctypes.windll.gdi32.DeleteObject(hfont)
    return size.cx, size.cy


class Textbox:
    rectangle = (0, 0, 0, 0)     # (x, y, width_X, length_Y)

    def __init__(self, start_pos, maximum_width, text, font_size, font):
        self.start_pos = start_pos
        self.maximum_width = maximum_width
        self.text = str(text)
        self.font_size = font_size
        self.font = font
        self.factor = gtd(text, font_size, font)[0] / maximum_width
        # self.arrange_rect()

    def arrange_rect(self):
        y_text = gtd(self.text[0], self.font_size, self.font)[1]
        if self.factor <= 1:
            Textbox.rectangle = (
                self.start_pos[0], self.start_pos[1], self.maximum_width, y_text)
        if self.factor > 1 and self.factor - int(self.factor) >= 0:
            Textbox.rectangle = (
                self.start_pos[0], self.start_pos[1], self.maximum_width, y_text * (int(self.factor) + 1))
        if self.factor > 1 and self.factor - int(self.factor) < 0:
            Textbox.rectangle = (
                self.start_pos[0], self.start_pos[1], self.maximum_width, y_text * int(self.factor))
        return Textbox.rectangle

    @staticmethod
    def shift_size(text, size, font, max_length, dec_by=1):

        fnt = pygame.font.SysFont(font, size)
        txt = fnt.render(text, True, (0, 0, 0))
        txt_dimension = gtd(text, size, font)
        if size == 0:
            print("text length is too large")
            return 1
        if dec_by > 0:
            if txt_dimension[0] > max_length:
                return Textbox.shift_size(text, size - dec_by, font, max_length, dec_by)
        if dec_by < 0:
            if txt_dimension[1] < max_length:
                return Textbox.shift_size(text, size - dec_by, font, max_length, dec_by)
        return size


class TextBoxInput:

    input = None
    current_input = ""
    write_enabled = False
    bar_pos = ()
    visible = True

    def __init__(self, surface, pos, width, height,
                 color=(255, 255, 255), border_color=(0, 0, 0), typeface='Arial', text_color=(0, 0, 0), mod=1,
                 button=True, button_length=None, button_text='Enter'):
        self.surface = surface
        self.pos = list(pos)
        self.width = width
        self.height = height
        self.typeface = typeface
        self.color = color
        self.border_color = border_color
        self.text_color = text_color
        self.mod = mod

        self.button = button
        self.button_length = button_length
        self.button_text = button_text

        self.size = Textbox.shift_size('A', 1, self.typeface, self.height-2, dec_by=-1)

        if self.button_length is None:
            self.button_length = self.width // 4

        if self.button:
            self.enter_button = Button(self.surface, (self.pos[0] + self.width, self.pos[1]),
                                       self.button_length, self.height, self.color, self.button_text, self.size,
                                       self.text_color, self.typeface, mod=2, border=self.border_color)

        self.bar_pos = (self.pos[0], self.pos[1] + 1)
        self.font = pygame.font.SysFont(self.typeface, self.size)

    def render(self):
        if self.visible:
            pygame.draw.rect(self.surface, self.border_color, (self.pos[0], self.pos[1]-1, self.width + 1,
                                                               self.height + 2))
            pygame.draw.circle(self.surface, self.border_color, [self.pos[0], self.pos[1] + self.height // 2],
                               self.height // 2 + 1)
            pygame.draw.circle(self.surface, self.border_color, [self.pos[0] + self.width,
                                                                 self.pos[1] + self.height // 2], self.height // 2 + 1)

            pygame.draw.circle(self.surface, self.color, [self.pos[0], self.pos[1] + self.height // 2], self.height//2)
            pygame.draw.circle(self.surface, self.color, [self.pos[0] + self.width, self.pos[1] + self.height // 2],
                               self.height // 2)
            pygame.draw.rect(self.surface, self.color, (self.pos[0], self.pos[1], self.width, self.height))

            self.enter_button.render()

            txt = self.font.render(self.current_input, True, self.text_color)
            txt_rect = txt.get_rect()

            self.surface.blit(txt, (self.pos[0], self.pos[1] - 1))

            if self.write_enabled:
                pygame.draw.line(self.surface, self.text_color, (self.pos[0] + txt_rect[2], self.pos[1] + 2),
                                 (self.pos[0] + txt_rect[2], self.pos[1] + txt_rect[3] - 2))

    def update(self, mouse_click):
        if self.collide() and mouse_click and self.visible:
            self.write_enabled = True

        if not self.collide() and mouse_click and self.visible:
            self.write_enabled = False

        if self.enter_button.clicked(mouse_click):
            self.write_enabled = False
            self.input = self.current_input

        self.enter_button.visible = self.visible

    def handle_keys(self, event):

        if event.type == pygame.KEYDOWN:
            if self.write_enabled:
                if event.key == 13:
                    self.write_enabled = False
                    self.input = self.current_input

                if event.key == 8 and len(self.current_input) >= 1:
                    l = list(self.current_input)

                    del l[len(l) - 1]
                    self.current_input = ''.join(l)

                elif event.key != 13 and event.key != 8:
                    self.current_input += event.unicode

    def collide(self):
        x, y = pygame.mouse.get_pos()

        if self.pos[0] <= x <= self.pos[0] + self.width and self.pos[1] <= y <= self.pos[1] + self.height \
                or (self.height // 2)**2 >= (self.pos[0] - x) ** 2 + (self.pos[1] - y + self.height // 2) ** 2 \
                or (self.height // 2)**2 >= (self.pos[0] + self.width-x)**2 + (self.pos[1]-y + self.height // 2)**2:
            return True
        return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 300), pygame.SRCALPHA)
    game_exit = False
    mouse_click = False
    textbox_input = TextBoxInput(screen, (50, 50), 200, 40, typeface='Arial', button=True, button_length=120)

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            textbox_input.handle_keys(event)
            mouse_click = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click = True

        screen.fill((255, 255, 255))
        textbox_input.render()
        textbox_input.update(mouse_click)
        if textbox_input.input is not None:
            print(textbox_input.input)
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()