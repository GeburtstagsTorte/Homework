import ctypes
import pygame


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
        txt_length = txt.get_rect()[2]
        if size == 0:
            print("text length is too large")
            return 1
        if txt_length > max_length:
            return Textbox.shift_size(text, size - dec_by, font, max_length, dec_by)
        return size


class TextBoxInput:

    def __init__(self):
        pass

    def render(self):
        pass

    def update(self):
        pass

    def handle_textbox_keys(self, event):
        pass
# Textbox((0, 50), 144, "to pee or not to pee", 10, "Arial")     # Textbox(start_pos, max_width, text, best_size, font)

# pygame.init()
# print(Textbox.shift_size("to be or not to be that is the question.", 15, "Courier New", 265, 1))
