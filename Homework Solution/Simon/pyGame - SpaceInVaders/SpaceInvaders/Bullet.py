from pygame import transform


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

    @staticmethod
    def shoot_bullet(bullet, game_display):
        bullet.render(game_display)
        bullet.update()
