import pygame
import math
from Constants import C

# F = G*m_1*m_2/ (d**2)


class Entities:

    particles = []
    attractors = []

    def __init__(self, screen):
        self.screen = screen

        self.particles = self.construct_particles()
        # [Particle(5, self.screen, (255, 0, 0), [C.width//2, C.height//2], [1, 0])]
        # self.construct_particles()
        self.attractors = self.construct_attractors()
        # self.construct_attractors()
        # [Attractor(5, self.screen, (255, 255, 255), [C.width//2, C.height//2 - 50]),
        #                   Attractor(5, self.screen, (255, 255, 255), [C.width // 2, C.height // 2 + 75])
        #                   ]

    def construct_particles(self):
        from random import randint

        particles = []
        for i in range(10):
            particles.append(
                Particle(1, self.screen, (255, 255, 255), [randint(0, C.width), randint(0, C.height)],
                         [randint(0, 5), randint(0, 5)])
            )
        return particles

    def construct_attractors(self):
        from random import randint
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
        # self.calculate_acc()
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius)

    def calculate_vel(self, pos):
        vector_pa = (pos[0] - self.pos[0], pos[1] - self.pos[1])
        distance = math.sqrt(vector_pa[0] ** 2 + vector_pa[1] ** 2)
        if distance == 0:
            distance += 1
        grav_force = (C.G * C.particle_mass * C.attractor_mass) / (distance ** 2)

        # acceleration vector
        acc = (vector_pa[0] * grav_force, vector_pa[1] * grav_force)

        self.vel[0] += acc[0]
        self.vel[1] += acc[1]

    def update(self, pos):
        self.calculate_vel(pos)
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        for i in range(len(self.pos)):
            self.pos[i] = int(self.pos[i])
        self.draw()
