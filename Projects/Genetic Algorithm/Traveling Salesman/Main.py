import pygame
from Constants import C
from Cities import City
from Population import Population
from Route import Route


class Game:
    clock = pygame.time.Clock()
    game_exit = False
    cities = []

    def __init__(self, title, width, height, background_color=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)

        self.cities = [City(self.game_display, self.width, self.height, C.city_color, C.city_radius)
                       for i in range(C.city_amount)]
        self.population = Population(C.max_population, C.mutation_rate, self.cities)

        self.main_loop()

    def main_loop(self):
        while not self.game_exit:

            for event in pygame.event.get():
                self.handle_keys(event)

            self.game_display.fill(self.background_color)
            self.render()
            pygame.display.update()
            self.update()
            self.clock.tick(60)

    def render(self):
        """for route in self.population.population:
            Route.draw_routes(self.game_display, C.route_color, route, self.cities)"""

        Route.draw_best_route(self.game_display, self.population.best, self.cities)
        City.render_cities(self.cities)

    def update(self):
        # Entities.update()
        self.population.update()

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True


def main():
    pygame.init()

    width = C.width
    height = C.height
    background_color = C.background_color
    Game("Genetic Algorithm - Traveling Salesman", width, height, background_color)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
