import pygame


class Button:

    def __init__(self, surface, x, y, width, height, color, text, font, text_size, text_color):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font = font
        self.text_size = text_size
        self.text_color = text_color

    def render(self):