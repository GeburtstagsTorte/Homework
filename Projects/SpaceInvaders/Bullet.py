from pygame import transform, Rect


class Bullet:

    bullet_speed = 8

    def __init__(self, pos_rect, collision_box, image):
        self.pos_rect = pos_rect
        self.collision_box = collision_box
        self.image = transform.scale(image, (int(pos_rect[2]), int(pos_rect[3])))

    def render(self, game_display):
        game_display.blit(self.image, self.pos_rect)

    def update(self):
        self.move()

    def move(self):
        self.pos_rect[1] -= Bullet.bullet_speed

    def get_true_collision(self):
        return Rect(self.pos_rect[0] + self.collision_box[0] / 100 * self.pos_rect[2],
                    self.pos_rect[1] + self.collision_box[1] / 100 * self.pos_rect[3],
                    self.collision_box[2] / 100 * self.pos_rect[2],
                    self.collision_box[3] / 100 * self.pos_rect[3],
                    )


class AlienBullet(Bullet):

    bullet_speed = 6

    def __init__(self, pos_rect, collision_box, image):
        super().__init__(pos_rect, collision_box, image)

    def move(self):
        self.pos_rect[1] += AlienBullet.bullet_speed


class SeismBomb(Bullet):

    bomb_speed = 3

    def __init__(self, pos_rect, collision_box, image):
        super().__init__(pos_rect, collision_box, image)

    def move(self):
        self.pos_rect[1] -= SeismBomb.bomb_speed
