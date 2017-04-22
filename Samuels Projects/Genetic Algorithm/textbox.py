import ctypes


def get_text_dimensions(text, points, font):   # thanks a lot anon :*
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
    rectangle = ((0, 0), 0, 0)     # (x, y, width_X, length_Y)

    def __init__(self, start_pos, maximum_width, text, font_size, font):
        self.start_pos = start_pos
        self.maximum_width = maximum_width
        self.text = str(text)
        self.font_size = font_size
        self.font = font
        self.factor = (len(text)*get_text_dimensions(text[0], font_size, font)[0]) / (maximum_width-start_pos[0])
        self.arrange_rect()

    def arrange_rect(self):
        y_text = get_text_dimensions(self.text[0], self.font_size, self.font)[1]
        if self.factor <= 1:
            Textbox.rectangle = (self.start_pos[0], self.start_pos[1], self.maximum_width, y_text)
        if self.factor > 1 and self.factor - int(self.factor) >= 0:
            Textbox.rectangle = (self.start_pos[0], self.start_pos[1], self.maximum_width // (int(self.factor) + 1),
                                 y_text * (int(self.factor) + 1))
        if self.factor > 1 and self.factor - int(self.factor) < 0:
            Textbox.rectangle = (
             self.start_pos[0], self.start_pos[1], self.maximum_width // int(self.factor), y_text * int(self.factor))
        return Textbox.rectangle

Textbox((0, 50), 144, "to pee or not to pee", 30, "Courier New")  # Textbox(start_pos, max_width, text, best_size, font)
                                                                  # richtige werte aus C usw wählen
