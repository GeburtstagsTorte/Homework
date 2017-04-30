import pygame


class Text:

    @staticmethod
    def shift_size(text, size, font, rect):
        font = pygame.font.SysFont(font, size)
        txt = font.render(text, True, (0, 0, 0))

        text_rect = txt.get_rect()[2], txt.get_rect()[3]

        while text_rect[0] > rect[0] or text_rect[1] > rect[1]:
            size -= 1
        return size
