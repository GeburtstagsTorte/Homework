import pygame
import math
from random import randint
from Constants import C
import pygame.gfxdraw
# F = G*m_1*m_2/ (d**2)


class Entities:

    particles = []
    attractors = []

    def __init__(self, screen):
        self.screen = screen

        self.particles = self.construct_particles()
        # self.construct_particles()
        # [Particle(1, self.screen, (255, 255, 255), [C.width//2, C.height//2], [1, 0])]
        # self.construct_particles()
        self.attractors = [Attractor(5, self.screen, (255, 255, 255), [C.width//2, C.height//2 - 150]),
                           Attractor(5, self.screen, (255, 255, 255), [C.width // 2, C.height // 2 + 150])
                           ]
        # self.construct_attractors()
        #
        # [Attractor(5, self.screen, (255, 255, 255), [C.width//2, C.height//2])]

    def construct_particles(self):
        # [randint(0, C.width), randint(0, C.height)]
        particles = []
        for i in range(5):
            particles.append(
                Particle(1, self.screen, C.particle_black, [C.width//2, C.height//2],
                         [randint(-3, 3), randint(-3, 3)])
            )
        return particles

    def construct_attractors(self):
        attractors = []

        for i in range(10):
            attractors.append(
                Attractor(5, self.screen, (255, 255, 255), [randint(0, C.width), randint(0, C.height)])
            )
        return attractors

    def update(self):
        for attractor in self.attractors:
            attractor.update()

        for particle in self.particles:
            for attractor in self.attractors:
                particle.update(attractor.pos)


class Attractor:
    def __init__(self, radius, surface, color, pos):
        self.radius = radius
        self.surface = surface
        self.color = color
        self.pos = pos

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius)

    def update(self):
        # self.draw()
        pass


class Particle:

    def __init__(self, radius, surface, color, pos, vel):
        self.radius = radius
        self.surface = surface
        self.color = color
        self.pos = pos
        self.vel = vel

    def draw(self):
        # pygame.draw.circle(self.surface, self.color, (int(round(self.pos[0])), int(round(self.pos[1]))), self.radius)
        pygame.gfxdraw.circle(self.surface, int(round(self.pos[0])), int(round(self.pos[1])), self.radius, self.color)

    def calculate_vel(self, pos):
        vector_pa = (pos[0] - self.pos[0], pos[1] - self.pos[1])
        distance = math.sqrt(vector_pa[0] ** 2 + vector_pa[1] ** 2)
        if distance == 0:
            distance += 1
        grav_magnitude = (C.G * C.particle_mass * C.attractor_mass) / (distance ** 2)

        # acceleration vector
        acc = (vector_pa[0] * grav_magnitude, vector_pa[1] * grav_magnitude)

        self.vel[0] += acc[0]
        self.vel[1] += acc[1]
        # print(acc)

    def update(self, pos):
        self.calculate_vel(pos)
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0] < -10000 or self.pos[0] > 10000 or self.pos[1] < -10000 or self.pos[1] > 10000:
            self.vel = [0, 0]

        # print(self.pos, (int(round(self.pos[0])), int(round(self.pos[1]))))
        self.draw()
