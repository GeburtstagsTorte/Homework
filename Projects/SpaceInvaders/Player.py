from pygame import transform, Rect
from Constants import Constants


class Player:

    dir_x = 0

    def __init__(self, draw_rect, collision_box, image, health):
        self.draw_rect = draw_rect
        self.collision_box = collision_box
        self.image = transform.scale(image, (int(draw_rect[2]), int(draw_rect[3])))
        self.health = health

    def render(self, game_display):
        game_display.blit(self.image, self.draw_rect)

    def update(self):
        if Constants.A:
            Player.dir_x = -6
        if Constants.D:
            Player.dir_x = 6
        self.move()

    def move(self):
        self.draw_rect[0] += Player.dir_x
        if self.draw_rect[0] >= Constants.WIDTH - Constants.player_size // 2:
            self.draw_rect[0] = 0
        elif self.draw_rect[0] <= 0:
            self.draw_rect[0] = Constants.WIDTH - Constants.player_size // 2
        Player.dir_x = 0

    def get_true_collision(self):
        return Rect(self.draw_rect[0] + self.collision_box[0] / 100 * self.draw_rect[2],
                    self.draw_rect[1] + self.collision_box[1] / 100 * self.draw_rect[3],
                    self.collision_box[2] / 100 * self.draw_rect[2],
                    self.collision_box[3] / 100 * self.draw_rect[3],
                    )
