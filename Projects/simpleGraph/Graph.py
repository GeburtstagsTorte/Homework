"""
    A simple graph, nothing special. It's rather a framework for following better graphs

"""

import pygame
# from GraphConstants import Constants as C


class SimpleGraph:

    def __init__(self, length, height, pos=(0, 0), step=1, style='default', caption=None, font='Courier New', size=10,
                 txt_color=(0, 0, 0), color=(0, 0, 0), stand_alone=False, values=None, units=None):
        """
            add Constant values in init
        """

        self.length = length
        self.height = height
        self.pos = pos
        self.step = step
        self.style = style
        self.caption = caption
        self.font = font
        self.size = size
        self.txt_color = txt_color
        self.color = color
        self.stand_alone = stand_alone
        self.values = values
        self.units = units

        self.x = pos[0]
        self.y = pos[1]

        self.origin = (self.pos[0] + C.border, self.pos[1] + C.border + self.height)

        self.show_dots = False

        if self.style == 'default':
            pass

        if self.caption is not None:
            font = pygame.font.SysFont(self.font, self.size)
            self.x_caption = font.render(self.caption[0], True, self.txt_color)
            self.y_caption = font.render(self.caption[1], True, self.txt_color)

        if self.stand_alone:
            pass

        self.transformed_values = sorted(self.transform_values(self.values, self.length, self.height, self.origin))

    def update(self):
        pass

    def render(self, surface=None):
        """
            optimize fluid rendering
        """
        if surface is None:
            return 'Error: No surface given.'

        # axis
        pygame.draw.line(surface, self.color, (self.pos[0] + C.border, self.pos[1] + C.border),
                         self.origin, C.axis_width)
        pygame.draw.line(surface, self.color, self.origin,
                         (self.pos[0] + self.length + C.border, self.pos[1] + C.border + self.height), C.axis_width)

        # render units
        self.render_units(surface)
        # render caption

        # render values
        if self.show_dots:
            self.render_values(surface)

        # connect values
        self.connect_values(surface)

    def render_units(self, surface=None):
        # x unit
        # if self.units is not None:
        x_ratio, y_ratio, max_x, max_y = SimpleGraph.unit(self.values, self.length, self.height)

        for i in range(int(max_x)):
            factor = int(x_ratio * (i + 1))
            pygame.draw.line(surface, self.color,
                             (self.origin[0] + factor, self.origin[1]), (self.origin[0] + factor, self.origin[1] +
                                                                         C.unit_length), C.axis_width)

        # y unit
        for i in range(int(max_y)):
            factor = int(y_ratio * (i + 1))
            pygame.draw.line(surface, self.color, (self.origin[0], self.origin[1] - factor),
                             (self.origin[0] - C.unit_length, self.origin[1] - factor), C.axis_width)
        # else:
        #    pass

        # text

    def render_values(self, surface=None):
        for value in self.transformed_values:
            pygame.draw.circle(surface, C.graph_color, value, C.graph_rad)

    def connect_values(self, surface=None):
        """
            sorting x values such that lowest x is first and highest x is last
            drawing lines where the first x value is the start pos and the second the end pos
        """

        for i in range(len(self.transformed_values)-1):
            pygame.draw.aaline(surface, self.color, self.transformed_values[i], self.transformed_values[i+1])

    @staticmethod
    def unit(values, length, height):
        max_x = 0
        max_y = 0
        for i in range(len(values)):
            if values[i][0] > max_x:
                max_x = values[i][0]
            if values[i][1] > max_y:
                max_y = values[i][1]

        return length / max_x, height / max_y, max_x, max_y

    @staticmethod
    def transform_values(values, length, height, origin):
        x_ratio = SimpleGraph.unit(values, length, height)[0]
        y_ratio = SimpleGraph.unit(values, length, height)[1]
        val = []
        for i in range(len(values)):
            x, y = values[i][0], values[i][1]
            val.append((origin[0] + int(x * x_ratio), origin[1] - int(y * y_ratio)))

        return val

    @staticmethod
    def check_values(x_values=None, y_values=None, values=None):

        if x_values is not None and y_values is not None:
            if len(x_values) == 0 or len(y_values) == 0:
                return 'Error: No values'

            elif len(x_values) != len(y_values):
                return 'Error: invalid value length'

            return x_values, y_values

        if values is not None:
            # Errors

            x_v = []
            y_v = []
            for i in range(len(values)):
                x_v.append(values[i][0])
                y_v.append(values[i][1])
            return x_v, y_v

        else:
            return 'Error: values incomplete'

    @staticmethod
    def import_values(file_name):
        x_values = []
        y_values = []

        file = open(file_name, 'r').read().splitlines

        for values in file:
            values.split(", ")
            x_values.append(float(values[0]))
            y_values.append(float(values[1]))

        return x_values, y_values


class C:
    # game
    width = 800
    height = 600

    axis_width = 2
    min_unit = 5
    unit_length = 5
    border = 5 + unit_length

    graph_color = (0, 102, 204)
    graph_rad = 2
